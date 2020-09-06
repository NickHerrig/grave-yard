import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import App from './App.vue'
import LoginComponent from './Login.vue'
import TodoComponent from './Todo.vue'

const router = new VueRouter({
    routes: [
        {
            path: '/',
            redirect: {
                name: "login"
            }
        },
        {
            path: "/login",
            name: "login",
            component: LoginComponent
        },
        {
            path: "/todo",
            name: "todo",
            component: TodoComponent
        }
    ]
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
