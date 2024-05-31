import streamlit as st
import time
import datetime

st.title(':green[Welcome] To :blue[_Adeoye_] Todolist. ✍️')

'''
 This is a personal todolist app which helps to keeps track of your task(s), in everyday life activities.

'''

'''
- Write an email to an organization, company and so on.📝
- Cooking a family meal at a specific time.🍽️
- Filling up an application for  interview.✍️
- Meeting up for an appointment hold by a board of directors.🤝                

'''


if 'uncompleted' not in st.session_state:
  st.session_state['uncompleted'] = {}

uncompleted = st.session_state['uncompleted']


if 'completed' not in st.session_state:
  st.session_state['completed'] = {}

completed = st.session_state['completed']


task_value = st.text_input("Enter the Task you want to do.", help="It will automatically add the new task in uncompleted TodoList.", placeholder='Enter your task.')

date = st.time_input('Enter the time to get this task started. ⌚')

dates = st.time_input('Enter the time to get this task completed. ⌚')

day = st.date_input('Enter the date of the task' , help="This helps you to ensure the deadline of the task you assigned to accomplished.")

add_task = st.button("Add Task")
if add_task:
  unique_key = f"{time.time()}"
  task_value = f'{task_value}. time: :green[{date}] ---- :red[{dates}] {day}'
  uncompleted[unique_key] = task_value

st.divider()
st.caption(" ## Uncompleted Tasks. ✖️✖️✖️")



# time.time()

def handle_click(key, task):
  if task == 'uncompleted':
    value = st.session_state['uncompleted'].pop(key)
    st.session_state['completed'][key] = value
  if task == 'completed':
    value = st.session_state['completed'].pop(key)
    st.session_state['uncompleted'][key] = value

if uncompleted.items():
  for key, task in uncompleted.items():
    st.checkbox(task, key=key, on_change=handle_click, args=(key, 'uncompleted',))
else:
  st.write(":grey[No current task(s).]")
 
st.divider()
st.caption("## Completed Tasks. ✅✅✅", help="When task in the uncompleted task is clicked it will be added in the completed task. ")



if completed.items():
  for key, task in completed.items():
    st.checkbox(task, key=key, value=True, on_change=handle_click, args=(key, 'completed',))
else:
  st.write(':grey[No current completed task(s).]')
