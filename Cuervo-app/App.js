import React from 'react';
import { Image } from 'expo-image';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import earthImage from './pictures/earth.jpg';

export default function App() {

  const [value, onChangeValue] = React.useState('Enter text here'); //do this so you can input a value
  const [InputValue, setInputValue] = React.useState('Input value here');

  const blurhash ='|rF?hV%2WCj[ayj[a|j[az_NaeWBj@ayfRayfQfQM{M|azj[azf6fQfQfQIpWXofj[ayj[j[fQayWCoeoeaya}j[ayfQa{oLj?j[WVj[ayayj[fQoff7azayj[ayj[j[ayofayayayj[fQj[ayayj[ayfjj[j[ayjuayj[';

  return (
    <View style={styles.box}>
      <View style={styles.box1}>
        <Text style ={styles.titleText}>WELCOME TO DMS-DD CONVERTER</Text>
      </View>
      <View style={styles.box2}>
        <View style={styles.box2_1}>
          <text>HELLO</text>
          <text>WORLD</text>
        </View>
        <View style={styles.box2_2}>
          <TextInput
            style={styles.input}
            onChangeText={setInputValue}
            value={InputValue}
          />
          <Button
            title = "Press me"
            onPress={()=>Alert.alert('Simple Button pressed')}
          />
        </View>
      </View>
      <View style={styles.box3}>
        <Text style ={styles.titleText}>Output:</Text>
        <Text style ={styles.titleText}>{value}</Text>
      </View>
      <View style={styles.box4}>
        <Image
          style={styles.Image}
          source={earthImage}
          placeholder={blurhash}
          contentFit="cover"
          transition={1000}
        />
      </View>
    </View>
  );
}


const styles = StyleSheet.create({
  box: {
    width: '100%',
    height: '100%',
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box1: {
    width: '100%',
    height: '10%',
    backgroundColor: 'pink',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box2: {
    width: '100%',
    height: '40%',
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box2_1: {
    flexDirection: 'column',
    width: '100%',
    height: '50%',
    backgroundColor: 'blue',
  },
  box2_2: {
    flex: 1,
    width: '100%',
    height: '50%',
    backgroundColor: 'red',
  },
  box3: {
    width: '100%',
    height: '25%',
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box4: {
    width: '100%',
    height: '25%',
    backgroundColor: 'pink',
    alignItems: 'center',
    justifyContent: 'center',
  },
  titleText: {
    fontSize: 24,
    fontWeight: '600'
  },
  Image: {
    flex: 1,
    width: '100%',
    backgroundColor: '#0553',
  },
  input: {
    width: '70%',
    height: '50%',
    fontSize: 24,
    color:'white',
  }
});
  