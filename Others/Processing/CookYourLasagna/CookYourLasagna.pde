class Lasagna { 
  
  Lasagna() {}
  
  int expectedMinutesInOven(){
    return 40;
  }
  
  int remainingMinutesInOven(int actualMinutes) { 
    return 40 - actualMinutes;
  }
  
  int preparationTimeInMinutes(int numLayers) { 
    return numLayers * 2;
  }
  
  int totalTimeInMinutes(int numLayers, int actualMinutes) { 
    return  preparationTimeInMinutes(numLayers) + remainingMinutesInOven(actualMinutes);
  }
  
}

Lasagna lasagna = new Lasagna();
println(lasagna.expectedMinutesInOven()); // => 40
println(lasagna.remainingMinutesInOven(30)); // => 10
println(lasagna.preparationTimeInMinutes(2)); // => 4
println(lasagna.totalTimeInMinutes(3, 20)); // => 26
