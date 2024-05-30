import React from 'react';
import { Image } from 'expo-image';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import earthImage from './pictures/earth.jpg';
import {Picker} from '@react-native-picker/picker';

export default function App() {

  const [OutputValue, setOutputValue] = React.useState('---'); //declare this constant variable so you can see the converted value
  const [InputValue, setInputValue] = React.useState('Input value here'); //declare this constant variable so you can input a value
  const [InputCase, setInputCase] = React.useState('Select Case');//declare this constant variable so you can select a case
  //declare this constant variable for the image to appear
  const blurhash ='|rF?hV%2WCj[ayj[a|j[az_NaeWBj@ayfRayfQfQM{M|azj[azf6fQfQfQIpWXofj[ayj[j[fQayWCoeoeaya}j[ayfQa{oLj?j[WVj[ayayj[fQoff7azayj[ayj[j[ayofayayayj[fQj[ayayj[ayfjj[j[ayjuayj[';

  // create a function for converting DD to DMS and DMS to DD
  function convertValue(value) {
    if (InputCase === "1") {
        // Convert DD to DMS
        var degrees = Math.floor(value);
        var minutes = Math.floor((value - degrees) * 60);
        var seconds = Math.round((value - degrees - (minutes / 60)) * 3600);
        var output = degrees.toString().concat("-", minutes.toString(), "-", seconds.toString());
        setOutputValue(output);
    } else if (InputCase === "2") {
        // Convert DMS to DD
        var elements = value.split("-");
        var output = parseFloat(elements[0]) + parseFloat(elements[1]) / 60 + parseFloat(elements[2]) / 3600;
        setOutputValue(output.toString());
    } else {
        // Handle invalid input case
        setOutputValue("Invalid Input Case");
    }
}

  return (
    // create a box for the heading, input, output, and footer
    <View style={styles.box}>
      <View style={styles.box1}>
        <Text style ={styles.titleText}>WELCOME TO DMS-DD CONVERTER</Text>
      </View>
      <View style={styles.box2}> 
        <View style={styles.box2_1}> 
          <text>INPUT CASE:</text>
          <Picker
            selectedValue={InputCase}
            onValueChange={(itemValue, itemIndex) =>
              setInputCase(itemValue)
            }>
            <Picker.Item label="DD TO DMS" value="1" />
            <Picker.Item label="DMS TO DD" value="2" />
          </Picker> 
        </View>
        <View style={styles.box2_2}>
          <TextInput 
            style={styles.input}
            onChangeText={setInputValue}
            value={InputValue}
          />
          <Button
            title = "Convert"
            onPress={()=>convertValue(InputValue)}
          />
        </View>
      </View>
      <View style={styles.box3}>
        <Text style ={styles.titleText1}>OUTPUT:</Text>
        <Text style ={styles.titleText1}>{OutputValue}</Text>
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

// create styles for each box and text
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
    backgroundColor: '#000829',
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
    backgroundColor: '#A8D1DF',
  },
  box2_2: {
    flex: 1,
    width: '100%',
    height: '50%',
    backgroundColor: '#A8D1DF',
  },
  box3: {
    width: '100%',
    height: '25%',
    backgroundColor: '#A8D1DF',
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
    fontWeight: '600',
    color: 'white'
  },
  titleText1: {
    fontSize: 24,
    fontWeight: '600',
    color: 'black'
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
    color:'black',
  }
});
  