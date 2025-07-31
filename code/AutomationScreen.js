import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ImageBackground } from 'react-native';

export default function AutomationScreen() {
  const [valveOn, setValveOn] = useState(false);
  const [lightOn, setLightOn] = useState(false);

  return (
    <ImageBackground
      source={require('../assets/background.jpg')}
      style={styles.background}
      resizeMode="cover"
    >
      <View style={styles.overlay}>
        <Text style={styles.header}>Automation Controls</Text>

        <TouchableOpacity
          style={[styles.button, valveOn ? styles.on : styles.off]}
          onPress={() => setValveOn(!valveOn)}
        >
          <Text style={styles.buttonText}>Smart Water Valve: {valveOn ? 'ON' : 'OFF'}</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, lightOn ? styles.on : styles.off]}
          onPress={() => setLightOn(!lightOn)}
        >
          <Text style={styles.buttonText}>Smart Light Bulb: {lightOn ? 'ON' : 'OFF'}</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: { flex: 1 },
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(255,255,255,0.6)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 30,
    color: '#003366',
    textAlign: 'center',
  },
  button: {
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    marginVertical: 12,
    width: '100%',
    alignItems: 'center',
    elevation: 2,
  },
  on: { backgroundColor: '#28a745' },
  off: { backgroundColor: '#dc3545' },
  buttonText: {
    fontSize: 18,
    color: '#fff',
    fontWeight: '600',
  },
});
