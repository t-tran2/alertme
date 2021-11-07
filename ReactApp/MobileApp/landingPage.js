import React, { Component } from "react";
import axios from 'axios';
import {
  View,
  Text,
  TouchableOpacity,
  TextInput,
  StyleSheet,
} from "react-native";

class LandingPage extends Component {
  state = {
    longitude: "",
    latitude: "",
    confirmedLocation: false,
  };
  updateLongitude = (text) => {
    this.setState({ longitude: text });
  };
  updateLatitude = (text) => {
    this.setState({ latitude: text });
  };
  submit = async (longitude, latitude) => {
    this.setState({ confirmedLocation: true });
      let response = await axios.get(`http://172.27.120.236:5000/alertme/?lat=${latitude}&long=${longitude}`);
      console.log(response.data);
      let data = response.data;
      console.log(JSON.stringify(response.data));
      let message
      if(!("warning" in response.data)){
        message = "Can't identify nearby roads."
      }
      else {
        message = response.data["warning"]
      }
      alert(message);
  };
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Welcome!</Text>
        <Text style={styles.subTitle}>
          Please type the longitude and latitude to continue
        </Text>
        <TextInput
          style={styles.input}
          underlineColorAndroid="transparent"
          placeholder="Longitude"
          placeholderTextColor="#9a73ef"
          autoCapitalize="none"
          onChangeText={this.updateLongitude}
        />

        <TextInput
          style={styles.input}
          underlineColorAndroid="transparent"
          placeholder="Latitude"
          placeholderTextColor="#9a73ef"
          autoCapitalize="none"
          onChangeText={this.updateLatitude}
        />

        <TouchableOpacity
          style={styles.submitButton}
          onPress={() => this.submit(this.state.longitude, this.state.latitude)}
        >
          <Text style={styles.submitButtonText}>
            {this.state.confirmedLocation ? "Update" : "Confirm"}
          </Text>
        </TouchableOpacity>
      </View>
    );
  }
}
export default LandingPage;

const styles = StyleSheet.create({
  title: {
    fontSize: 35,
  },
  subTitle: {
    marginBottom: 20,
    fontSize: 15,
  },
  input: {
    padding: 5,
    width: "50%",
    margin: 15,
    height: 40,
    borderColor: "#7a42f4",
    borderWidth: 1,
  },
  submitButton: {
    backgroundColor: "#7a42f4",
    padding: 10,
    margin: 15,
    height: 40,
  },
  submitButtonText: {
    color: "white",
  },
  container: {
    flex: 1,
    backgroundColor: "white",
    alignItems: "center",
    justifyContent: "center",
  },
});
