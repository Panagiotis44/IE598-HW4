import numpy as np

def vcg_allocation(n_agents, m_goods):
    # Generate random valuations for each agent for each good
    valuations = np.random.rand(n_agents, m_goods)
    
    # Calculate the social surplus for each allocation
    social_surplus = []
    for i in range(m_goods):
        allocation_without_agent_i = np.delete(valuations, i, axis=1)
        max_value_without_i = np.amax(allocation_without_agent_i, axis=0)
        social_surplus.append(np.sum(max_value_without_i))
    
    # Calculate each agent's externality for each good
    externality = np.zeros((n_agents, m_goods))
    for i in range(n_agents):
        for j in range(m_goods):
            allocation_without_agent_i = np.delete(valuations, i, axis=0)
            max_value_without_i = np.amax(allocation_without_agent_i[:, j])
            externality[i][j] = max_value_without_i
    
    # Calculate each agent's payment
    payments = []
    for i in range(n_agents):
        payment_i = np.sum(externality[i]) - social_surplus
        payments.append(payment_i)
    
    # Calculate each agent's utility
    utilities = []
    for i in range(n_agents):
        utility_i = np.sum(valuations[i]) - payments[i]
        utilities.append(utility_i)
    
    # Allocate goods to agents
    allocations = {}
    for i in range(m_goods):
        allocation_without_agent_i = np.delete(valuations, i, axis=1)
        max_value_without_i = np.amax(allocation_without_agent_i, axis=0)
        allocated_agent = np.argmax(max_value_without_i)
        allocations[i] = allocated_agent
    
    # Calculate social welfare after allocation
    social_welfare = 0
    for good, agent in allocations.items():
        social_welfare += valuations[agent][good]
    
    # Calculate revenue
    revenue = 0
    for good, agent in allocations.items():
        revenue += payments[agent][good]
    
    return valuations, social_surplus, externality, payments, utilities, social_welfare, allocations, revenue

for m in range(2,21):
    for n in range(2,21):
        repeats=10000
        total_welfare=0
        total_revenue=0
        for i in range(repeats):
            n_agents = n
            m_goods = m

            valuations, social_surplus, externality, payments, utilities, social_welfare, allocations, revenue = vcg_allocation(n_agents, m_goods)
            total_welfare+=social_welfare
            total_revenue+=revenue
        expected_welfare=total_welfare/repeats
        expected_revenue=total_revenue/repeats
        print("for ",m," items and ",n," agents the expected social welfare is: ",expected_welfare," and the expected revenue is: ",expected_revenue)
    






"""
print("Agent valuations for goods:")
print(valuations)
print("\nSocial surplus for each good:")
print(social_surplus)
print("\nExternality for each agent for each good:")
print(externality)
print("\nPayments from each agent:")
print(payments)
print("\nUtilities for each agent:")
print(utilities)
print("\nSocial welfare:")
print(social_welfare)
print("\nAllocations:")
for good, agent in allocations.items():
    print(f"Good {good+1} allocated to Agent {agent+1}")
print("\nRevenue:")
print(revenue)"""

