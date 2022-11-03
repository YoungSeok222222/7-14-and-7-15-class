<template>
  <div class="backborder">
    <h1>AppParent</h1>
    <input type="number" id="parentnum" v-model.number="parentnum" @input="GoToApp">
   <p>appData: {{ appNum }}</p>
   <p>childData: {{ childNum }}</p>
    
   <AppChild :parent-num="parentnum" :app-num="appNum" 
   @child-num="InputChildData"
   />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
    name : 'AppParent',
    data(){
        return {
          parentnum : 0,
          childNum : 0,
        }
    },
    components : {
      AppChild,
    },
    props : {
      appNum : Number,
    },
    methods : {
      InputChildData : function(childnum) {
        this.childNum = childnum
        this.$emit('child-num', this.childNum)
      },
      GoToApp : function(){
        this.$emit('parent-num', this.parentnum)
      }
    },

}
</script>

<style >
  .backborder{
    border: solid 1px orange;
  }
</style>