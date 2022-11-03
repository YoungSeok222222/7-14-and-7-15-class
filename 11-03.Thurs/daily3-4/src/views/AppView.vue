<template>
  <div class="blackborder">
    <h1>App</h1>
    <input type="number" id="appnum" v-model.number="appnum">
    <p>parentData: {{parentNum}}</p>
    <p>childData: {{ childnum }}</p>

    <AppParent :app-num="appnum" @parent-num="getInfo" @child-num="getChild" />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent.vue'
export default {
    name : 'AppView',
    data () {
        return {
            appnum : 0,
            parentNum: 0,
            childnum: 0,
        }
    },
    components : {
        AppParent,
    },
    methods:{
      getInfo: function(parentnum) {
        this.parentNum = parentnum
      },
      getChild: function(childnum) {
        this.childnum = childnum
      }
    }

}
</script>

<style>
  .blackborder{
    border: solid 1px black;
  }
</style>