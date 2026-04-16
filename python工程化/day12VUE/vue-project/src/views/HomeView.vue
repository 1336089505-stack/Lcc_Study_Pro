<template>
  <div>
    <p>原始金额：{{ amount }}</p>
    <p>税后金额：{{ computedAmount }}</p>
  </div>
</template>


<script>
export default {
  data() {
    return {
      amount: 100
    };
  },
  computed: {
    computedAmount() {
      return this.amount * 1.1; // 假设税率为10%
    }
  }
};
</script>

