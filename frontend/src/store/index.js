import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import defaultImage from "../pages/image/default.png";
export default createStore({
  state: {
    predictedPrice: 0,
    predictedPriceRange: []
  },
  mutations: {
    initializedStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token');
        state.username = localStorage.getItem('username');
        state.isAuthenticated = true;
        state.profilePic = defaultImage
        // console.log("Username "+state.username + " Token "+state.token)
      } else {
        state.token = '';
        state.username = '';
        state.isAuthenticated = false;
        state.profilePic = defaultImage
        console.log("Resetting Username "+state.username + " Token "+state.token)
      }
    },
    setToken(state, token, username) {
      state.token = token;
      state.username = username;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
      state.username = '';
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
  plugins: [createPersistedState()],
});
