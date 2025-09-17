import React, { useEffect, useState } from 'react';
import {
  View, Text, StyleSheet, SafeAreaView,
  ActivityIndicator, ImageBackground, Dimensions, ScrollView
} from 'react-native';
import { LineChart } from 'react-native-chart-kit';
import { Picker } from '@react-native-picker/picker';

export default function SensorScreen() {
  const [data, setData] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedChart, setSelectedChart] = useState('temperature');
  const [predictions, setPredictions] = useState({});

  const fetchData = async () => {
    try {
      const response = await fetch('http://192.168.1.192:5000/data');
      const json = await response.json();
      setData(json);
      setLoading(false);
    } catch (error) {
      console.log('Fetch error:', error);
      setLoading(false);
    }
  };

  const fetchHistory = async () => {
    try {
      const response = await fetch('http://192.168.1.192:5000/history');
      const historyData = await response.json();
      setHistory(historyData);
    } catch (error) {
      console.log('History fetch error:', error);
    }
  };

  const linearPrediction = (values) => {
    const n = values.length;
    if (n < 2) return [values[n - 1]];

    const last = values[n - 1];
    const secondLast = values[n - 2];
    const delta = last - secondLast;

    return [
      parseFloat((last + delta).toFixed(2)),
      parseFloat((last + 2 * delta).toFixed(2)),
      parseFloat((last + 3 * delta).toFixed(2))
    ];
  };

  const calculatePredictions = () => {
    const temp = history.map(e => e.temperature);
    const hum = history.map(e => e.humidity);
    const rad = history.map(e => e.solar_radiation);
    const prec = history.map(e => e.precipitation);

    setPredictions({
      temperature: linearPrediction(temp),
      humidity: linearPrediction(hum),
      solar_radiation: linearPrediction(rad),
      precipitation: linearPrediction(prec),
    });
  };

  useEffect(() => {
    fetchData();
    fetchHistory();
    const interval = setInterval(() => {
      fetchData();
      fetchHistory();
    }, 60000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (history.length > 1) calculatePredictions();
  }, [history]);

  const graphData = {
    temperature: history.map(e => e.temperature),
    humidity: history.map(e => e.humidity),
    solar_radiation: history.map(e => e.solar_radiation),
    precipitation: history.map(e => e.precipitation),
  };

  return (
    <ImageBackground
      source={require('../assets/background.jpg')}
      style={styles.background}
      resizeMode="cover"
    >
      <ScrollView contentContainerStyle={styles.overlay}>
        <Text style={styles.header}>Libelium Sensor Dashboard</Text>

        {loading ? (
          <ActivityIndicator size="large" color="#007bff" />
        ) : (
          <View style={styles.card}>
            <Text style={styles.label}>🌡️ Temperature: <Text style={styles.value}>{data.temperature} °C</Text></Text>
            <Text style={styles.label}>💧 Humidity: <Text style={styles.value}>{data.humidity} %</Text></Text>
            <Text style={styles.label}>☀️ Solar Radiation: <Text style={styles.value}>{data.solar_radiation} W/m²</Text></Text>
            <Text style={styles.label}>🌧️ Precipitation: <Text style={styles.value}>{data.precipitation} mm</Text></Text>
            <Text style={styles.timestamp}>⏱️ Last Update: {data.timestamp}</Text>
          </View>
        )}

        {/* Predicted values */}
        {Object.keys(predictions).length > 0 && (
          <View style={styles.predictionCard}>
            <Text style={styles.predictionTitle}> Predicted Values (next 3 min)</Text>
            {Object.entries(predictions).map(([key, values]) => (
              <Text key={key} style={styles.label}>
                {key.charAt(0).toUpperCase() + key.slice(1)}: {values.join(' / ')}
              </Text>
            ))}
          </View>
        )}

        {/* Dropdown selector */}
        <View style={styles.pickerWrapper}>
          <Picker
            selectedValue={selectedChart}
            onValueChange={(itemValue) => setSelectedChart(itemValue)}
            style={styles.picker}
          >
            <Picker.Item label="🌡️ Temperature" value="temperature" />
            <Picker.Item label="💧 Humidity" value="humidity" />
            <Picker.Item label="☀️ Solar Radiation" value="solar_radiation" />
            <Picker.Item label="🌧️ Precipitation" value="precipitation" />
          </Picker>
        </View>

        {/* Chart */}
        {graphData[selectedChart].length > 1 && (
          <LineChart
            data={{
              labels: [],
              datasets: [{ data: graphData[selectedChart] }]
            }}
            width={Dimensions.get('window').width - 40}
            height={220}
            yAxisSuffix={selectedChart === 'precipitation' ? ' mm' : selectedChart === 'solar_radiation' ? ' W/m²' : selectedChart === 'humidity' ? ' %' : ' °C'}
            chartConfig={{
              backgroundGradientFrom: '#e0f7fa',
              backgroundGradientTo: '#80deea',
              decimalPlaces: 1,
              color: (opacity = 1) => `rgba(0, 51, 102, ${opacity})`,
              labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
              style: { borderRadius: 16 },
              propsForDots: { r: '4', strokeWidth: '2', stroke: '#007bff' },
            }}
            bezier
            style={{ marginVertical: 16, borderRadius: 16 }}
          />
        )}
      </ScrollView>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: { flex: 1 },
  overlay: {
    flexGrow: 1,
    backgroundColor: 'rgba(255,255,255,0.6)',
    padding: 20,
    alignItems: 'center',
  },
  header: {
    fontSize: 24,
    marginBottom: 30,
    fontWeight: 'bold',
    color: '#003366',
    textAlign: 'center',
  },
  card: {
    backgroundColor: 'white',
    borderRadius: 16,
    padding: 24,
    width: '100%',
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 8,
    elevation: 4,
  },
  label: {
    fontSize: 18,
    marginVertical: 8,
    color: '#333',
  },
  value: {
    fontWeight: 'bold',
    color: '#007bff',
  },
  timestamp: {
    marginTop: 10,
    fontSize: 14,
    color: '#777',
    textAlign: 'center',
  },
  predictionCard: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 16,
    marginTop: 24,
    width: '100%',
  },
  predictionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#003366',
    marginBottom: 10,
    textAlign: 'center',
  },
  pickerWrapper: {
    marginTop: 24,
    backgroundColor: '#fff',
    borderRadius: 12,
    width: '100%',
  },
  picker: {
    height: 50,
    width: '100%',
  },
});

