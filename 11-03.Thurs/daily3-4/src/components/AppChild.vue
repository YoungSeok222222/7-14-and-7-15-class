<template>
  <div class="border">
    <h1>AppChild</h1>
    <input type="number" v-model="childnum" @input="GoToParent" >
    <p>appData: {{ appNum }}</p>
    <p>parentData: {{ parentNum }}</p>
    <p>childNum: {{ childnum }}</p>

  </div>
</template>

<script>
export default {
    name : 'AppChild',
    props : {
        parentNum : Number,
        appNum : Number
    },
    data(){
        return {
            childnum : 0,
        }
    },
    methods: {
        GoToParent: function(){
            this.$emit('child-num', this.childnum)
        }
    }
}
</script>

<style >
  .border{
    border : solid 1px blue;
  }
</style>