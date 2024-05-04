import random

class Agent:
    def __init__(self, weight, bid):
        self.weight = weight
        self.bid = bid

def knapsack_auction(agents, W):
    agents = [agent for agent in agents if agent.weight <= W]  # Exclude agents with weight > W
    agents.sort(key=lambda x: x.bid / x.weight, reverse=True)
    total_weight = 0
    total_bid = 0
    max_bid = 0
    selected_agents = []
    ratios = []

    for agent in agents:
        ratio = agent.bid / agent.weight
        ratios.append(ratio)

        if total_weight + agent.weight <= W:
            selected_agents.append(agent)
            total_weight += agent.weight
            total_bid += agent.bid
            max_bid = max(max_bid, agent.bid)
        else:
            break

    # Check if the maximum bid of the remaining agents can fit in the knapsack
    for agent in agents:
        if agent.bid > max_bid and agent.weight <= W:
            selected_agents = [agent]
            total_weight = agent.weight
            total_bid = agent.bid
            break

    total_welfare = sum(agent.weight * agent.bid for agent in selected_agents)    

    return total_bid, total_welfare, selected_agents, ratios

if __name__ == "__main__":
    for k in range(5,31):
        count_bid=0
        count_welfare=0
        repeats=10000
        for j in range(repeats):
            n = k
            agents = [Agent(random.randint(1, 20), random.randint(0, 100)) for _ in range(n)]
            #print("Weights and bids of agents:")
            """for i, agent in enumerate(agents):
                print(f"Agent {i+1}: Weight={agent.weight}, Bid={agent.bid}")"""

            W = 10  # Total weight capacity of the knapsack

            total_bid, total_welfare, selected_agents, ratios = knapsack_auction(agents, W)
            #print("Total bid of selected agents:", total_bid)
            #print("Total revenue of the knapsack:", total_revenue)
            #print("Agents assigned to the knapsack:")
            """for agent in selected_agents:
                print(f"Weight={agent.weight}, Bid={agent.bid}")
            
            print("Bid-to-weight ratios of agents:")
            for i, ratio in enumerate(ratios):
                print(f"Agent {i+1}: Ratio={ratio:.2f}")"""
            count_bid=count_bid+total_bid
            count_welfare=count_welfare+total_welfare

        print("expected revenue for ",n, "number of agents: ",count_bid/repeats," and the excpected social welfare is: ",count_welfare/repeats)