import random
import math
import matplotlib.pyplot as plt

# -----------------------------
# Pure ALOHA Simulation
# -----------------------------

SIMULATION_TIME = 1000        # seconds
PACKET_TIME = 1.0             # transmission time
NUM_STATIONS = 20             # number of users
MAX_BACKOFF = 5               # random retransmission delay

loads = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.4,1.6,1.8,2.0]

simulated_throughput = []
theoretical_throughput = []

for G in loads:

    events = []

    # Generate packets for every station
    for station in range(NUM_STATIONS):

        t = random.expovariate(G / NUM_STATIONS)

        while t < SIMULATION_TIME:
            events.append({
                "station": station,
                "start": t,
                "end": t + PACKET_TIME,
                "success": True
            })

            t += random.expovariate(G / NUM_STATIONS)

    # Sort packets according to transmission time
    events.sort(key=lambda x: x["start"])

    # Collision Detection
    for i in range(len(events)):

        for j in range(i + 1, len(events)):

            if events[j]["start"] >= events[i]["end"]:
                break

            # Collision occurs
            events[i]["success"] = False
            events[j]["success"] = False

    successful = sum(1 for p in events if p["success"])
    collided = len(events) - successful

    throughput = successful * PACKET_TIME / SIMULATION_TIME

    simulated_throughput.append(throughput)
    theoretical_throughput.append(G * math.exp(-2 * G))

    print("-----------------------------------")
    print(f"Load (G)            : {G:.2f}")
    print(f"Packets Generated   : {len(events)}")
    print(f"Successful Packets  : {successful}")
    print(f"Collided Packets    : {collided}")
    print(f"Throughput          : {throughput:.3f}")
    print("-----------------------------------")

# -----------------------------
# Plot Results
# -----------------------------

plt.figure(figsize=(8,5))

plt.plot(loads,
         simulated_throughput,
         'bo-',
         linewidth=2,
         label='Simulation')

plt.plot(loads,
         theoretical_throughput,
         'r--',
         linewidth=2,
         label='Theory (G*e^-2G)')

plt.xlabel("Offered Load (G)")
plt.ylabel("Throughput (S)")
plt.title("Pure ALOHA Simulation")

plt.grid(True)
plt.legend()

plt.show()