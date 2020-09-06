<template>
  <div id="app">
    <div id="nav">
      <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link>
    </div>
    <router-view @login:user="authenticateUser" />
  </div>
</template>

<script>
  export default {
    name: 'app',
    data() {
      return {
        authenticated: false, 
        mockAccounts:[
          {
            email: "me@mail.com",
            password: "me",
            id: 1
          },
          {
            email: "you@mail.com",
            password: "you",
            id: 2
          },
        ]
      }
    },
    mounted() {
      if(!this.authenticated) {
        this.$router.replace({ name: "login"});
      }
    },
    methods: {
      authenticateUser(user) {
        var found = this.mockAccounts.find(function(post) {
          if (post.email == user.email && post.password == user.password)
            return true;
        });
        
        if (typeof found !== "undefined") {
          this.authenticated = true;
          this.$router.push({ name: "todo", params: { id: found.id }});
        } else {
            this.authenticated = false;
        }
      },
      logout() {
        this.authenticated = false;
      }
    } 
  }
</script>

<style>
  body {
    background-color: #F0F0F0;
  }
  h1 {
    padding: 0;
    margin-top: 0;
  }
  #app {
    width: 1024px;
    margin: auto;
  }
</style>
