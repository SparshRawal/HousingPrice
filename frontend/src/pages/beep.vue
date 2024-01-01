<template>
    <!-- <div class="contaier-fluid bg_image" > -->
  
    <div class="col-sm-12">
      <div class="mb-3 row">
        <h1 class="text-center text-primary">Beep Page</h1>
      </div>
      <form @submit.prevent="logOut">
        <div class="mb-3 row">
          <div class="mb-3 col-sm-4"></div>
          <div class="mb-3 col-sm-3" v-if="this.$store.state.isAuthenticated">
            <button class="container-fluid btn btn-outline-success disabled">Logged In</button>
          </div>
          <div class="mb-3 col-sm-3" v-if="this.$store.state.isAuthenticated">
            <button class="container-fluid btn btn-outline-danger">Log Out</button>
          </div>
          <div class="mb-3 col-sm-4" v-else>
            <router-link to="/login">
              <button class="container-fluid btn btn-outline-success">Login</button>
            </router-link>
          </div>
          <div>
          <button class="container-fluid btn btn-outline-success" v-on:click="playSound">
            Hello
          </button>
        </div>
        </div>
      </form>
    </div>
    <!-- </div> -->
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'HomePage',
    mounted() {
      this.checkAutentication();
    },
    methods: {
        playSound()
        {
            // var audio = new Audio('http://soundbible.com/mp3/Elevator Ding-SoundBible.com-685385892.mp3');
            const sound = require("../components/logos/beep.mp3");
            var audio = new Audio(sound);
            // const getMP3Duration = require('get-mp3-duration')
            // const buffer = fs.readFileSync('sound')
            // const duration = getMP3Duration(audio)
            console.log(audio.duration)
            audio.play();
        },
      checkAutentication() {
        if (this.$store.state.isAuthenticated) {
          this.username = localStorage.getItem('username');
          console.log(this.$store.state.isAuthenticated);
          console.log('Hello Checking Auth ' + this.username);
        } else {
          this.username = '';
          console.log(this.$store.state.isAuthenticated);
          console.log('Hello Checking Auth ' + this.username);
        }
      },
      logOut() {
        console.log();
        const formData = {
          token: localStorage.getItem('token'),
        };
        axios.defaults.headers.common['Authorization'] = 'Token ' + formData.token;
        axios
          .post('/api/v1/token/logout', formData)
  
          .then(response => {
            console.log(response);
            //const token = response.data.auth_token
            //console.log(token)
            this.$store.commit('removeToken');
            //axios.defaults.headers.common['Authorization'] = "Token "+token
            //localStorage.setItem('token',token)
            //localStorage.setItem('username',this.username)
            //onsole.log(localStorage.getItem('username'))
            localStorage.setItem('token', '');
            this.$router.push('/');
          })
          .catch(error => {
            console.log(error);
          });
      },
    },
    data() {
      return {
        message: 'Hello',
        username: '',
      };
    },
  };
  </script>
  
  <style lang="scss">
  @import '../styles/theme.scss';
  </style>
  