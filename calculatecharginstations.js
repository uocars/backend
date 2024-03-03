class Main {
    chargingstations(model, distance) {
      let stationsAmount = 0;
      if (model === "Mach-E") {
        const maxRange = 402;
        const rangeUse = 320;
        stationsAmount = Math.floor(distance / rangeUse);
        console.log(stationsAmount);
      } else if (model === "F-150 Lightning") {
        const maxRange = 386;
        const rangeUse = 306;
        stationsAmount = Math.floor(distance / rangeUse);
        console.log(stationsAmount);
      }
      return stationsAmount;
    }
  }
  
  // Example usage:
  const chargingStations1 = new Main().chargingstations("Mach-E", 800);