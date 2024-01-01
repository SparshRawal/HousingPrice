import { createApp } from 'vue'
import App from './App'
import 'bootstrap';
import router from './router';
import store from './store';
import axios from 'axios';
import './styles/theme.scss';

import VueGeolocation from "vue3-geolocation";
import GMaps from "vuejs3-google-maps";
import VueGoogleMaps from '@fawmi/vue-google-maps';

axios.defaults.baseURL = 'http://127.0.0.1:8000'

// createApp(App).use(store).use(router).mount('#app')


let app = createApp(App);

app.use(VueGeolocation);
app.use(GMaps, {
  load: {
    apiKey: "AIzaSyD3ZmhwN_l5Yg29sjlI6qQrPZt55sNsOpo",
    libraries: ["places"],
  },
});
app.use(VueGoogleMaps, {
    load: {
      key: 'AIzaSyD3ZmhwN_l5Yg29sjlI6qQrPZt55sNsOpo',
      libraries: "places"
    },
  });
app.use(store)
app.use(router)

app.mount("#app");