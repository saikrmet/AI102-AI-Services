### Container Deployment in Azure AI Services

#### What is a Container?
- **Definition**: A container includes an application or service with all the runtime components it needs, while abstracting the underlying OS and hardware.
- **Benefits**:
  - **Portability**: Containers can be moved across different hosts, regardless of the operating system or hardware.
  - **Isolation**: A single host can run multiple isolated containers, each with its own runtime configuration.
- **Container Image**: Encapsulates the software and configuration. Images can be stored in central registries like Docker Hub or in private registries.

#### Container Deployment Process
- **Steps**:
  1. **Pull Image**: Download the container image from a registry.
  2. **Deploy**: Deploy the image to a container host, such as in the cloud, on a private network, or locally.
  3. **Configure**: Apply any required configuration settings for the container.

- **Examples of Container Hosts**:
  - Docker server
  - Azure Container Instance (ACI)
  - Azure Kubernetes Service (AKS)

#### Using Azure AI Services Containers
1. **Deploy the Container**: Download and deploy the container image for the specific Azure AI services API (from sources like Microsoft Container Registry).
2. **Client Interaction**: Applications submit data to the container’s endpoint and retrieve results, similar to how they interact with Azure AI services in the cloud.
3. **Usage Metrics**: The container sends usage data to Azure for billing purposes.

- **Endpoint Management**:
  - Applications must use the container-specific endpoint instead of the Azure cloud endpoint.
  - **Requests do not require a key, meaning anyone with the ACI IP address or FQDN can hit the service. To prevent this, containers are deployed in VNets so only certain IPs can make requests.**