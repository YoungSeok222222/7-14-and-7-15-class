import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CalculatorView from '../views/CalculatorView.vue'
import AppView from '../views/AppView.vue'
import YoutubeView from '../views/YoutubeView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path : '/calculator',
    name  : 'taxCalculator',
    component : CalculatorView
  },
  {
    path: '/app',
    name :'appView',
    component : AppView
  },
  {
    path : '/ssafytube',
    name : 'ssafyTube',
    component : YoutubeView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
