<template>
  <div id="nav">
    <router-link to="/"></router-link>
    <router-link to="/register"></router-link>
  </div>
  <router-view />
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      username: localStorage.getItem('username'),
    };
  },
  beforeCreate() {
    this.$store.commit('initializeStore');

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token;
    } else {
      axios.defaults.headers.common['Authorization'] = '';
    }
  },
  updated() {
    this.username = localStorage.getItem('username');
    console.log('Hello ' + this.username);
  },
  methods: {
    logOut() {
      console.log();
      const formData = {
        token: localStorage.getItem('token'),
      };
      console.log("Logging out ",formData.token)
      axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token');
      axios
        .post('/api/v1/token/logout', formData)

        .then(response => {
          console.log(response);
          this.$store.commit('removeToken');
          localStorage.setItem('token', '');
          localStorage.setItem('username', '');
          location.reload()
          this.$router.push('/')
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss">
@import './styles/theme.scss';
</style>
