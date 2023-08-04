from censys.search import CensysHosts

# Create a CensysHosts instance
h = CensysHosts()

# Define a query to search for China hosts using Nginx Software over HTTP
query_string = "services.software.product: nginx AND services.service_name: HTTP AND location.country=China"

# Iterate through the search results
query = h.search(query_string, per_page=50, page=1, virtual_hosts="INCLUDE") # Adjust the number of results
for page in query:
    for host in page:
        print(host)