import * as tf from '@tensorflow/tfjs';

// Definicja modelu regresji liniowej
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));

// Przygotowanie modelu do treningu: Okresl strate i optymalizator.
model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

// Generuje syntetyczne dane do treningu
const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

// Trenuj model używając danych
model.fit(xs, ys, {epochs: 10}).then(() => {
  // Użyj modelu, aby wykonać wnioskowanie na punkcie danych, którego model jeszcze nie widział:
  model.predict(tf.tensor2d([5], [1, 1])).print();
});