<!-- <template>
  <div>
    <h1>Products</h1>
    <table class="table">
      <thead>
        <tr>
          <th style="text-align: right">product</th>
          <th>price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td style="text-align: right">{{ product.name }}</td>
          <td>{{ product.price }}</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th style="text-align: right">Total</th>
          <th>{{ totalItem }}</th>
        </tr>
      </tfoot>
    </table>
  </div>
</template>
<script>
import axios from 'axios';

const endpoint = 'http://backend:8000';

export default {
  name: 'ProductsList',
  data() {
    return {
      products: []
    }
  },
  created() {
    axios.get(endpoint + '/api')
      .then(response => {
        this.products = response.data.data
      })
  },
  computed: {
    totalItem() {
      let sum = 0;
      this.products.forEach(function (item) {
        sum += parseFloat(item.price);
      });
      return sum.toFixed(2);
    }
  }
}
</script>
<style scoped>
.table {
  border-collapse: collapse;
  width: 30%;
  margin-left: auto;
  margin-right: auto;
}

thead th {
  border-bottom: 2px solid #ddd;
}

tbody th,
td {
  border-bottom: 1px solid #ddd;
}

th,
td {
  padding: 15px;
  text-align: left;
}

tbody tr:hover {
  background-color: #f5f5f5;
}

tfoot tr {
  border-top: 2px solid #ddd;
}
</style> -->

<template>
  <div>
    <h1>Products</h1>
    <table class="table">
      <thead>
        <tr>
          <th style="text-align: right">product</th>
          <th>price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td style="text-align: right">{{ product.name }}</td>
          <td>{{ product.price }}</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th style="text-align: right">Total</th>
          <th>{{ totalItem }}</th>
        </tr>
      </tfoot>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

// Update endpoint to match the new API path
const endpoint = '/api'; // Base URL

export default {
  name: 'ProductsList',
  data() {
    return {
      products: []
    }
  },
  created() {
    // Adjust the API path here to the new route
    axios.get(`${endpoint}/`)
      .then(response => {
        console.log(response.data);
        this.products = response.data.data;
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  },
  computed: {
    totalItem() {
      return this.products
        .reduce((sum, item) => sum + parseFloat(item.price), 0)
        .toFixed(2);
    }
  }
}
</script>

<style scoped>
.table {
  border-collapse: collapse;
  width: 30%;
  margin-left: auto;
  margin-right: auto;
}

thead th {
  border-bottom: 2px solid #ddd;
}

tbody th,
td {
  border-bottom: 1px solid #ddd;
}

th,
td {
  padding: 15px;
  text-align: left;
}

tbody tr:hover {
  background-color: #f5f5f5;
}

tfoot tr {
  border-top: 2px solid #ddd;
}
</style>
