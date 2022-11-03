<template>
<div>
  <h1>소득세 계산기</h1>

  <div>
    <label for="income">연봉 입력(만 원):</label>
    <input type="number" id="income" v-model.number="income">
  </div>

  <div>
    <label for="tax-credit">세액감면액(만 원):</label>
    <input type="number" id="tax-credit" v-model.number="taxCredit">
  </div>

  <hr>

  <TotalIncome :income="income" :tax-credit="taxCredit" />
</div>

</template>

<script>
import TotalIncome from '@/components/TotalIncome';
export default {
  name : 'CalculatorView',
  data() {
    return {
      income : 0,
      taxCredit : 0,
    }
  },
  components : {
    TotalIncome,
  }

}


</script>

<style>

</style>