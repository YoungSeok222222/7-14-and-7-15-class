import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HellowView from '@/views/HellowView'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'


Vue.use(VueRouter)
const isLoggedIn = false
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component:HellowView
  },
  {
    path:'/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path:'/login',
    name:'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인함')
        next({name:'home'})
      } else{
        next()
      }
    }
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next)=> {
//   // 로그인 여부
//   const isLoggedIn = false

//   //로그인이 필요한 페이지
//   // const authPages = ['hello','home','about']
//   const allowAllPages = ['login']

//   //앞으로 이동할 페이지(to)가
//   //로그인이 필요한 사이트인지 확인
//   const isAuthRequired = !allowAllPages.includes(to.name)
  
//   if (isAuthRequired && !isLoggedIn) {
//     console.log('login으로 이동!')
//     next({name: 'login'})
//   } else{
//     console.log('to로 이동')
//     next()
//   }
// })

export default router
