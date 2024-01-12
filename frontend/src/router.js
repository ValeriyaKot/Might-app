import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import CreateBadge from './views/CreateBadge.vue'
import AssignBadge from './views/AssignBadge.vue'



Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
            path: '/',
            component: Home
        },
        {
            path: '/:groupId/add',
            component: CreateBadge
        },
        {
            path: '/:employeeId/assign',
            component: AssignBadge
        }
    ]
})