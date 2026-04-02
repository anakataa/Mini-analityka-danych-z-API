import streamlit as st
import requests
import pandas as pd
import plotly.express as px


# CONFIGURATION & UI SETUP

st.set_page_config(page_title="Cogitech - Mini Analityka", layout="wide")

st.title("Mini-analityka danych z API (JSONPlaceholder)")
st.markdown("Projekt realizuje pełen zakres wymagań zadania dla **Cogitech**. Przetwarza dane z 4 endpointów, wylicza 4 metryki oraz prezentuje 2 wykresy.")


# PART 1: FETCHING DATA FROM API

# using cache to prevent unnecessary API calls on every app rerun
@st.cache_data
def fetch_data(endpoint):
    url = f"https://jsonplaceholder.typicode.com{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data from {endpoint}")
        return []

with st.spinner("Pobieranie danych z API..."):
    users_data = fetch_data("/users")
    posts_data = fetch_data("/posts")
    comments_data = fetch_data("/comments")
    todos_data = fetch_data("/todos")

# converting json responses into pandas dataframess for easier manipulationn
df_users = pd.DataFrame(users_data)
df_posts = pd.DataFrame(posts_data)
df_comments = pd.DataFrame(comments_data)
df_todos = pd.DataFrame(todos_data)


# PART 2: PROCESSING DATA & CALCULATING METRICS

st.header("Główne Metryki")

# Metric 1: Average number of posts per user
total_users = len(df_users)
total_posts = len(df_posts)
avg_posts_per_user = total_posts / total_users if total_users > 0 else 0

# Metric 2: Average number of comments per post
total_comments = len(df_comments)
avg_comments_per_post = total_comments / total_posts if total_posts > 0 else 0

# Metric 3: Percentage of completed TODOs
total_todos = len(df_todos)
completed_todos = len(df_todos[df_todos['completed'] == True])
percent_completed_todos = (completed_todos / total_todos) * 100 if total_todos > 0 else 0

# Displaying the first 3 metrics in a row
col1, col2, col3 = st.columns(3)
col1.metric("Średnia postów na użytkownika", f"{avg_posts_per_user:.1f}")
col2.metric("Średnia komentarzy na post", f"{avg_comments_per_post:.1f}")
col3.metric("Wykonane TODOs", f"{percent_completed_todos:.1f}%")

st.write("---")

# Metric 4: Top 5 most commented posts
st.subheader("Top 5 najbardziej komentowanych postów")


comments_count = df_comments.groupby('postId').size().reset_index(name='liczba_komentarzy')

merged_top_posts = pd.merge(comments_count, df_posts[['id', 'title']], left_on='postId', right_on='id')
# Sorting in descending order and taking the top 5
top_5_posts = merged_top_posts.sort_values(by='liczba_komentarzy', ascending=False).head(5)

top_5_posts = top_5_posts[['title', 'liczba_komentarzy']].rename(columns={'title': 'Tytuł posta', 'liczba_komentarzy': 'Liczba komentarzy'})

# Displaying the top 5 posts as a dataframe inside the app
st.dataframe(top_5_posts, use_container_width=True, hide_index=True)

st.write("---")


# PART 3: VISUALIZING THE RESULTS

st.header("Wizualizacje")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Aktywność użytkowników")
    
    # bar chart: number of posts per user
    posts_count_user = df_posts.groupby('userId').size().reset_index(name='post_count')
    merged_user_posts = pd.merge(posts_count_user, df_users[['id', 'name']], left_on='userId', right_on='id')
    
    fig_bar = px.bar(merged_user_posts, x='name', y='post_count', 
                     labels={'name': 'Użytkownik', 'post_count': 'Liczba postów'},
                     color='post_count', color_continuous_scale='Blues')
    st.plotly_chart(fig_bar, use_container_width=True)

with col_chart2:
    st.subheader("Procent wykonanych zadań (TODOs)")
    
    # pie chart: TODOs status distribution
    todo_status = df_todos['completed'].value_counts().reset_index()
    todo_status.columns = ['Status', 'Liczba']
    todo_status['Status'] = todo_status['Status'].map({True: 'Wykonane', False: 'Niewykonane'})
    
    fig_pie = px.pie(todo_status, values='Liczba', names='Status', 
                     color='Status', color_discrete_map={'Wykonane':'#00CC96', 'Niewykonane':'#EF553B'})
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.caption("Stworzone przez Kirilla Staroshchuka dla Cogitech.")