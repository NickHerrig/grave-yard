<template>
  <div id="todo-form">
    <form @submit.prevent="handleSubmit">
      <input 
        ref="first"
        type="text"
        :class="{ 'has-error': submitting && invalidName }"
        v-model="task.title"
        @focus="clearStatus"
        @keypress="clearStatus"
      />
      <button class="addtask" >Add Task</button>
      <p v-if="error && submitting" class="error-message">
        Please fill out a Task!
      </p>
      <p v-if="success" class="success-message">
        Task successfully created!
      </p>
      <div class="divider"/>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'todo-form',
    data() {
      return {
        submitting: false,
        error: false, 
        success: false,
        task: {
          title: '',
        },
      }
    },
    methods: {
      handleSubmit() {
        this.submitting = true
        this.clearStatus()

        if (this.invalidTitle) {
          this.error = true
          return
        }

        this.$emit('add:task', this.task)
        this.$refs.first.focus()
        this.task = {
          title: '',
        }
        this.error = false
        this.success = true 
        this.submitting = false
      },
      clearStatus() {
        this.error = false
        this.success = false

      },
    },
    computed: {
      invalidTitle() {
        return this.task.title == ''
      }
    }
  }
</script>

<style scoped>
form {
  margin-bottom: 2rem;
}

[class*='-message'] {
  font-weight: 500;
}

.error-message {
  color: #de373c
}

.success-message {
  color: #40db79
}

.divider{
    width:5px;
    height:auto;
    display:inline-block;
}

button{
    display:inline-block;
    padding:0.46em 1.6em;
    border:0.1em solid #000000;
    margin:0 0.2em 0.2em 0;
    border-radius:0.12em;
    box-sizing: border-box;
    text-decoration:none;
    font-family:'Roboto',sans-serif;
    font-weight:300;
    color:#000000;
    text-shadow: 0 0.04em 0.04em rgba(0,0,0,0.35);
    background-color:#FFFFFF;
    text-align:center;
    transition: all 0.15s;
}
button:hover{
    text-shadow: 0 0 2em rgba(255,255,255,1);
    color:#FFFFFF;
    border-color:#FFFFFF;
}

</style>
