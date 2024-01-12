import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import '../scss/custom.scss'
import '../vee-validate'


Vue.config.productionTip = false
Vue.config.devtools = true
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
    el: '#app',
    router,
    render: h => h(App)
}).$mount('#app');
