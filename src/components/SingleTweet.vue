<template>
  <v-form ref="form">
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="12" sm="6" md="3">
              <v-text-field prepend-inner-icon="mdi-card-text" v-model="text" :rules="[rules.required, rules.counter]"  counter maxlength="250"  label="Paste tweet body"
              ></v-text-field><v-btn @click="getTweetText" color="primary">Analyse!</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
  import * as tf from '@tensorflow/tfjs';

  export default {
    data(){
      return {
        text: '',
        modelLoaded: false,
        modelJSON: require('../model/jsmodel/model.json'),
        tokenizer: require('../model/tokenizer.json'),
        rules: {
          required: value => !!value || 'Required.',
          counter: value => value.length <= 250 || 'Max 250 characters',
        },
      }
    },
  mounted(){
    this.loadModel();
  },
  methods: {
      async loadModel(){
        this.model = await tf.loadLayersModel(this.modelJSON)
      },
      stringCleaner(text){
        return text.toLowerCase().trim().replace(/@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+/g, " ").split(" ");
      },
      tokenizedArray(arrayText){
        let tokens = []      
        arrayText.forEach(element => {
          if(this.tokenizer[element])
            tokens.push(this.tokenizer[element])
          else
            tokens.push(this.tokenizer['<OOV>'])
        });
        return tokens;
      },
      padArray(arrayTokens){
        const maxlength = 300;
        if (arrayTokens.length < maxlength) {
          let pad_array = Array(maxlength - arrayTokens.length);
          pad_array.fill(this.tokenizer['<OOV>']);
          arrayTokens = arrayTokens.concat(pad_array);
        }
        return arrayTokens;
      },
      predict(arrayTokensPadded){
        let inputTensor = tf.tensor(arrayTokensPadded);
        this.model.then(model => {
          let result = model.predict(inputTensor);
          result = result.round().dataSync()[0];
          alert(result ? "possitive" : "negative");
        });
      },
      getTweetText(){
        if(this.$refs.form.validate()){
          let stringCleaned = this.stringCleaner(this.text);
          let tokens = this.tokenizedArray(stringCleaned);
          let arrayTokensPadded = this.padArray(tokens);
          this.predict(arrayTokensPadded);
          console.log(stringCleaned+"->"+tokens);
          console.log(arrayTokensPadded);
        }
      }
    }

  }
</script>
