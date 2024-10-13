# Data-preprocessing-using-Apache-Spark
The primary goal for this project is to use Apache Spark for data preprocessing and exploratory data analysis (EDA) to enhance efficiency and minimize processing time.

In my Python program for preprocessing and exploratory data analysis, I started by addressing missing values using imputation techniques. For numerical values, I applied mean imputation, while for categorical values, I used mode imputation. Next, I checked for duplicate records in the dataset and removed any duplicates found to ensure data integrity. To explore the data, I plotted histograms to visualize the distribution of numerical predictors and used bar plots to analyze the frequency distribution of categorical predictors. Additionally, I created boxplots to check for outliers among numerical features. Finally, I generated a correlation matrix to examine the relationships between predictors and the response variable, which is the exam score, allowing me to identify highly correlated predictors that could be significant for further analysis.

I will be usign to VMs in this project, so I configured my two VMs and installed and configured Apache spark.

First let me generate ssh key pair for connection between the two vms (master and worker)
I generated ssh key pair in hadoop1 then copied the key to the other vm (hadoop 2)


Ssh-keygen -t rsa

cat.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

Then I configure Spark in the cluster mode.

I user tar spark package on hadoop1 and scp to hadoop2

On hadoop1

cd /opt

tar czf spark.tar.gz spark

scp spark.tar.gz root@hadoop2:/opt

On hadoop2

cd /opt

tar  xvzf  spark.tar.gz

To start spark

/opt/spark/sbin/start-all.sh

To submit a spark job I used Command     

-- /opt/spark/bin/spark-submit --master spark://hadoop1:7077 /opt/preprocessing.py



Performance of the program

I observed that the duration for completing the action using only 1 Vm was approximately 2.4 minutes. When I ran the command again to check for consistency, the time remained almost the same at 2.3 minutes. This indicates that running the Python code on a single VM (using Hadoop 1 only) consistently takes about 2.4 minutes.

The duration for completing a specific action using two VMs was about 27 seconds. This is approximately five times faster than the time taken when using only one VM, which was around 2.4 minutes. Running the Python code using both VMs (Hadoop 1 and Hadoop 2) demonstrates a significant improvement in processing speed.


