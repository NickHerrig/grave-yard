<template>
  <div id="login" class="login">
    <div class="login-triangle"></div>
    <h2 class="login-header">Please log in</h2>

    <form @submit.prevent="handleLogin" class="login-container">
      <p><input 
        ref="first"
        placeholder="Email Address"
        type="email"
        required=""
        v-model="user.email"
        @focus="clearStatus"
        @keypress="clearStatus"
      /></p>
      <p><input 
        type="password"
        placeholder="Password"
        required=""
        v-model="user.password"
        @focus="clearStatus"
        @keypress="clearStatus"
      /></p>
      <p><input type="submit" value="Log in"></p>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data() {
      return {
        submitting: false,
        error: false, 
        success: false,
        user: {
          email: '',
          password: '',
        },
      }
    },
    methods: {
      handleLogin() {
        this.submitting = true
        this.clearStatus()

        this.$emit('login:user', this.user)
        this.$refs.first.focus()
        this.user = {
          email: '',
          password: ''
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
  }
</script>

<style scoped>
/* 'Open Sans' font from Google Fonts */
@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700);

body {
  background: #456;
  font-family: 'Open Sans', sans-serif;
}

.login {
  width: 400px;
  margin: 16px auto;
  font-size: 16px;
}

/* Reset top and bottom margins from certain elements */
.login-header,
.login p {
  margin-top: 0;
  margin-bottom: 0;
}

/* The triangle form is achieved by a CSS hack */
.login-triangle {
  width: 0;
  margin-right: auto;
  margin-left: auto;
  border: 12px solid transparent;
  border-bottom-color: #28d;
}

.login-header {
  background: #28d;
  padding: 20px;
  font-size: 1.4em;
  font-weight: normal;
  text-align: center;
  text-transform: uppercase;
  color: #fff;
}

.login-container {
  background: #ebebeb;
  padding: 12px;
}

/* Every row inside .login-container is defined with p tags */
.login p {
  padding: 12px;
}

.login input {
  box-sizing: border-box;
  display: block;
  width: 100%;
  border-width: 1px;
  border-style: solid;
  padding: 16px;
  outline: 0;
  font-family: inherit;
  font-size: 0.95em;
}

.login input[type="email"],
.login input[type="password"] {
  background: #fff;
  border-color: #bbb;
  color: #555;
}

/* Text fields' focus effect */
.login input[type="email"]:focus,
.login input[type="password"]:focus {
  border-color: #888;
}

.login input[type="submit"] {
  background: #28d;
  border-color: transparent;
  color: #fff;
  cursor: pointer;
}

.login input[type="submit"]:hover {
  background: #17c;
}

/* Buttons' focus effect */
.login input[type="submit"]:focus {
  border-color: #05a;
}
</style>
