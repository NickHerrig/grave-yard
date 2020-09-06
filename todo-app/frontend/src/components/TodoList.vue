<template>
  <div id="todo-list">
    <ul v-for="task in tasks" :key="task.task_id">

      <li v-if="editing === task.task_id">
        <input type="text" v-model="task.title"/>
      </li>

      <li v-else-if="task.completed">✅  {{ task.title }}</li>

      <li v-else>{{ task.title }}</li>

      <div v-if="editing === task.task_id">
        <button class="save" @click="editTask(task)">
          Save 
        </button>
        <div class="divider"/>
        <button class="cancel" @click="cancelEdit(task)">
          Cancel
        </button>
      </div>

      <div v-else-if="task.completed">
        <button class="edit" @click="editMode(task)">
          Edit
        </button>
        <div class="divider"/>
        <button class="delete" @click="$emit('delete:task', task.task_id)">
          Delete
        </button>
      </div>

      <div v-else>
        <button class="complete" @click="setComplete(task)">
          Completed
        </button>
        <div class="divider"/>
        <button class="edit" @click="editMode(task)">
          Edit
        </button>
        <div class="divider"/>
        <button class="delete" @click="$emit('delete:task', task.task_id)">
          Delete
        </button>
      </div>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'todo-list',
    props: {
      tasks: Array,
    },
    data() {
      return {
        editing: null,
      }
    },
    methods: {
      editMode(task) {
        this.cachedTask = Object.assign({}, task)
        this.editing = task.task_id
      },

      setComplete(task) {
        task.completed = 1;
        this.editTask(task);
      },
      cancelEdit(task) {
        Object.assign(task,this.cachedTask)
        this.editing = null;
      },

      editTask(task) {
        if (task.title === '') return
        this.$emit('edit:task', task.task_id, task)
        this.editing = null
      },
    }
  }
</script>

<style scoped>
ul {
  list-style-type: none;
  border:1px solid #000;
  padding:10px 0;
  font-size: 24px;
}

.divider{
  width:5px;
  height:auto;
  display:inline-block;
}

button{
  display:inline-block;
  padding:0.3em 1.2em;
  margin:0 0.1em 0.1em 0;
  border:0.16em solid rgba(255,255,255,0);
  border-radius:2em;
  box-sizing: border-box;
  text-decoration:none;
  font-weight:300;
  color:#FFFFFF;
  text-shadow: 0 0.04em 0.04em rgba(0,0,0,0.35);
  text-align:center;
  transition: all 0.2s;
}

button:hover{
  border-color: rgba(255,255,255,1);
}

button.delete{
  background-color:#f14e4e
}

button.complete{
  background-color:#32a852
}

button.edit{
  background-color:#9a4ef1
}

button.cancel{
  background-color:#f1bb4e
}

button.save{
  background-color:#f14ebd
}

</style>

