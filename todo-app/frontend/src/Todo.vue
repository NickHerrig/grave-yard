<template>
  <div id="todo">
    <h1>Todo List</h1>

    <todo-form @add:task="addTask" />

    <todo-list
      :tasks="tasks"
      @delete:task="deleteTask"
      @edit:task="editTask"
    ></todo-list>
  </div>
</template>

<script>
  import TodoList from './components/TodoList.vue'
  import TodoForm from './components/TodoForm.vue'

  export default {
    name: 'todo',
    components: {
      TodoList,
      TodoForm,
    },

    data() {
      return {
        tasks: [],
      }
    },

    mounted() {
      this.getTasks()
    },

    methods: {
      async getTasks() {
        try {
          const response = await fetch('https://{domain}:{port}/task',
          {
            method: 'GET',
            headers: {
            'Content-type': 'application/json',
            'Set-Cookie': 'authenticatedUserID=' + this.$route.params.id
            }
          })
          const data = await response.json()
          this.tasks = data
        } catch (error) {
          console.error(error)
        }
      },
      async addTask(task) {
        try {
          const response = await fetch('https://{domain}:{port}/task', 
          {
            method: 'POST',
            body: JSON.stringify(task),
            headers: {
              'Content-type': 'application/json',
              'Set-Cookie': 'authenticatedUserID=' + this.$route.params.id
            },
          })
          const data = await response.json()
          this.tasks = [...this.tasks, data]
        } catch (error) {
          console.error(error)
        }
      },
      async deleteTask(id) {
        try {
          await fetch(`https://{domain}:{port}/task/${id}`,
          { method: "DELETE" });
          this.tasks = this.tasks.filter(task => task.task_id !== id);
        } catch (error) {
          console.error(error);
        }
      },
      async editTask(id, updatedTask) {
        try {
          const response = await fetch(`https://{domain}:{port}/task/${id}`, 
          {
            method: 'PUT',
            body: JSON.stringify(updatedTask),
            headers: {'Content-type': 'application/json'},
          })
          const data = await response.json()
          this.tasks = this.tasks.map(task => (task.task_id == id ? data : task))
        } catch (error) {
          console.error(error)
        }
      },
    }
  }
</script>

<style>
#todo {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
