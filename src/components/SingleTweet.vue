<template>
  <v-container
    class="fill-height"
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col cols="12" sm="6" md="3">
            <v-text-field label="Paste tweet body"
            ></v-text-field><v-btn @click="getTweetText" color="primary">Analyse!</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    data(){

    },
    methods: {
      getTweetText(){
        console.log("Activado!")
      }
    }

  }
</script>
