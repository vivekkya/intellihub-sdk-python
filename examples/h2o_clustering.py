import intellihub


def main():
    c = intellihub.IntellihubClient('xxx')

    cluster_data_store_response = c.store('../csv/moon_data.csv')
    print(cluster_data_store_response)
    cluster_data = cluster_data_store_response['fileUrl']

    cluster_response = c.cluster("clustering", "KMeansClustering", cluster_data, ["X", "Y"], "h2o", 2,
                                 "Clustering Model", True)
    print(cluster_response)
    cluster_job_status_response = c.job_status(cluster_response['data']['jobId'])
    print(cluster_job_status_response)
    cluster_job_output_response = c.job_output(cluster_response['data']['jobId'])
    print(cluster_job_output_response)

    pred_file = cluster_job_output_response['output']['clusterFileUrl']
    response = c.download(pred_file)
    print(response.text)


if __name__ == '__main__':
    main()