# Results :memo: :detective:
## Capacity of the Hopfield network
The following graphs represents the capacity of the hopfield network to retrieve patterns that werer perturbed at 20%. The x-axis representing the number of patterns and  the y-axis being the probability of retrieving them. 
For the Hebbian rule the covergence for a given network size and number of pattern was controlled 100 times and 10 times for the Storkey rule being very time consuming. The more itterations there are, the more the results correspond to the expected ones.

![100 iteration frac](https://user-images.githubusercontent.com/114407059/209163578-48856282-6ec5-425e-8ed1-040b61082383.png)

![strokey match_frac](https://user-images.githubusercontent.com/114407059/209352511-69fbd633-35aa-4440-be01-e4f5747388e6.png)

The following graphe represents the theoretical capacity of a network using the **Hebbian learning rule** given by : $C_{H} = \frac{n}{2log(n)}$ versus the one we obtained running our system.

![100 iteration capcity](https://user-images.githubusercontent.com/114407059/209337526-9a04d52d-e1c2-49ae-ad34-1ff8a633c838.png)

This graph represents the theoretical capacity of a network using the **Storkey learning rule** given by : $C_{S} = \frac{n}{\sqrt{2log(n)}}$.

![strokey capacity](https://user-images.githubusercontent.com/114407059/209352472-ec6f9946-8d30-4ac2-9291-413a9c0020f6.png)

## Robustness to perturbations :muscle:
The follwowing graph represents the percentage of perturbation that a network can sustain versus the fraction of retrieval of the pattern.

![robustness 100](https://user-images.githubusercontent.com/114407059/209164020-4f5b0963-4b86-472c-91a1-570d951faabe.png)

![robustness storkey](https://user-images.githubusercontent.com/114407059/209352537-a51926a1-37d5-4991-893b-85887cafd359.png)
 
## Recalling image content from corrupted images :camera:

Few examples of 100x100 image binarized and represented as 10000 neurons pattern using "binarize_img" function in hopfield_network.py. This additional function automatically binarizes the images given. The function "binarize_img" accepts colorful pictures and contrasts them in black and white. Any format image is accepted by "binarize_img". We use hebbian matrix and dynamics rule for image reconstruction.

To binarize an image use the folowing command in the main (image has to be 100x100) : 
<pre><code>im = h.binarize_img("image_name", save = False)</code></pre>



### Random perturbations images
These first few examples shows the different step realized by the programm: images given, perturbed images and the covergence step images.

<img width="835" alt="hockey final" src="https://user-images.githubusercontent.com/114407059/208116190-99ca281d-bf8c-4e72-aaf8-bb4e2f7996a3.png">
<img width="835" alt="tigre final " src="https://user-images.githubusercontent.com/114407059/208116254-30956e1f-e746-4c2f-b4ad-cf17f700a97b.png">
<img width="835" alt="velo final" src="https://user-images.githubusercontent.com/114407059/208116276-a94679fe-c94f-4be3-9662-a6ddac3300cd.png">
<img width="835" alt="zebre final " src="https://user-images.githubusercontent.com/114407059/208116282-b8e6b659-0b50-4d7b-8f86-1ef89bdceff7.png">

The recalling image from random pertubations image part can be use by uncommenting the line
<pre><code>recalling_from_random_perturb_images("name_image")</code></pre>

in the [experience.py](https://github.com/EPFL-BIO-210/BIO-210-22-team-13/blob/sanspoo/experience.py) file and running this file. The name_image is the image name with his format and must be changed.


### Corrupted images
These figures are the same images but the perturbations are not random anymore. This time, the complete images are recalled by an incomplete subsets of herself.

<img width="835" alt="image" src="https://user-images.githubusercontent.com/55958594/208940797-82f37214-53cd-459c-8dbf-8ae356024a94.png">
<img width="835" alt="image" src="https://user-images.githubusercontent.com/55958594/208940841-c708c3cf-cd81-49e7-9679-964a31f0938e.png">
<img width="835" alt="image" src="https://user-images.githubusercontent.com/55958594/208940866-e48ad064-24b6-45a4-af23-d818d47c5f04.png">
<img width="835" align ="center" alt="image" src="https://user-images.githubusercontent.com/55958594/208940889-4c665293-a377-457a-b9eb-8a84c92375b4.png">

The recalling image from corrupted image part can be use by uncommenting the line
<pre><code>recalling_from_corrupted_images("name_image")</code></pre>

in the [experience.py](https://github.com/EPFL-BIO-210/BIO-210-22-team-13/blob/sanspoo/experience.py) file and running this file. The name_image is the image name with his format and must be changed.




## Datas regarding the capacity :panda_face:

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  0 |             10 | Hebbian        |              1 |             2 |         1    |
|  1 |             10 | Hebbian        |              1 |             2 |         1    |
|  2 |             10 | Hebbian        |              1 |             2 |         1    |
|  3 |             10 | Hebbian        |              2 |             2 |         0.8  |
|  4 |             10 | Hebbian        |              2 |             2 |         0.8  |
|  5 |             10 | Hebbian        |              2 |             2 |         0.81 |
|  6 |             10 | Hebbian        |              3 |             2 |         0.47 |
|  7 |             10 | Hebbian        |              3 |             2 |         0.45 |
|  8 |             10 | Hebbian        |              3 |             2 |         0.52 |
|  9 |             10 | Hebbian        |              4 |             2 |         0.21 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 10 |             18 | Hebbian        |              1 |             3 |         1    |
| 11 |             18 | Hebbian        |              2 |             3 |         1    |
| 12 |             18 | Hebbian        |              2 |             3 |         0.99 |
| 13 |             18 | Hebbian        |              3 |             3 |         0.85 |
| 14 |             18 | Hebbian        |              3 |             3 |         0.83 |
| 15 |             18 | Hebbian        |              4 |             3 |         0.57 |
| 16 |             18 | Hebbian        |              4 |             3 |         0.65 |
| 17 |             18 | Hebbian        |              5 |             3 |         0.41 |
| 18 |             18 | Hebbian        |              5 |             3 |         0.43 |
| 19 |             18 | Hebbian        |              6 |             3 |         0.19 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 20 |             34 | Hebbian        |              2 |             6 |         1    |
| 21 |             34 | Hebbian        |              3 |             6 |         0.97 |
| 22 |             34 | Hebbian        |              4 |             6 |         0.9  |
| 23 |             34 | Hebbian        |              4 |             6 |         0.94 |
| 24 |             34 | Hebbian        |              5 |             6 |         0.81 |
| 25 |             34 | Hebbian        |              6 |             6 |         0.6  |
| 26 |             34 | Hebbian        |              7 |             6 |         0.51 |
| 27 |             34 | Hebbian        |              8 |             6 |         0.39 |
| 28 |             34 | Hebbian        |              8 |             6 |         0.31 |
| 29 |             34 | Hebbian        |              9 |             6 |         0.21 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 30 |             63 | Hebbian        |              3 |            12 |         1    |
| 31 |             63 | Hebbian        |              5 |            12 |         0.99 |
| 32 |             63 | Hebbian        |              6 |            12 |         0.94 |
| 33 |             63 | Hebbian        |              7 |            12 |         0.89 |
| 34 |             63 | Hebbian        |              8 |            12 |         0.82 |
| 35 |             63 | Hebbian        |             10 |            12 |         0.58 |
| 36 |             63 | Hebbian        |             11 |            12 |         0.51 |
| 37 |             63 | Hebbian        |             12 |            12 |         0.35 |
| 38 |             63 | Hebbian        |             13 |            12 |         0.25 |
| 39 |             63 | Hebbian        |             15 |            12 |         0.13 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 40 |            116 | Hebbian        |              6 |            23 |         1    |
| 41 |            116 | Hebbian        |              8 |            23 |         1    |
| 42 |            116 | Hebbian        |             10 |            23 |         0.99 |
| 43 |            116 | Hebbian        |             12 |            23 |         0.93 |
| 44 |            116 | Hebbian        |             14 |            23 |         0.75 |
| 45 |            116 | Hebbian        |             16 |            23 |         0.62 |
| 46 |            116 | Hebbian        |             18 |            23 |         0.37 |
| 47 |            116 | Hebbian        |             20 |            23 |         0.25 |
| 48 |            116 | Hebbian        |             22 |            23 |         0.13 |
| 49 |            116 | Hebbian        |             24 |            23 |         0.09 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 50 |            215 | Hebbian        |             10 |            43 |         1    |
| 51 |            215 | Hebbian        |             13 |            43 |         0.99 |
| 52 |            215 | Hebbian        |             16 |            43 |         0.99 |
| 53 |            215 | Hebbian        |             20 |            43 |         0.94 |
| 54 |            215 | Hebbian        |             23 |            43 |         0.85 |
| 55 |            215 | Hebbian        |             26 |            43 |         0.58 |
| 56 |            215 | Hebbian        |             30 |            43 |         0.38 |
| 57 |            215 | Hebbian        |             33 |            43 |         0.25 |
| 58 |            215 | Hebbian        |             36 |            43 |         0.16 |
| 59 |            215 | Hebbian        |             40 |            43 |         0.03 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 60 |            397 | Hebbian        |             16 |            79 |         1    |
| 61 |            397 | Hebbian        |             22 |            79 |         1    |
| 62 |            397 | Hebbian        |             27 |            79 |         0.98 |
| 63 |            397 | Hebbian        |             33 |            79 |         0.92 |
| 64 |            397 | Hebbian        |             38 |            79 |         0.8  |
| 65 |            397 | Hebbian        |             44 |            79 |         0.62 |
| 66 |            397 | Hebbian        |             49 |            79 |         0.42 |
| 67 |            397 | Hebbian        |             55 |            79 |         0.17 |
| 68 |            397 | Hebbian        |             60 |            79 |         0.08 |
| 69 |            397 | Hebbian        |             66 |            79 |         0.05 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 70 |            733 | Hebbian        |             27 |           146 |         1    |
| 71 |            733 | Hebbian        |             37 |           146 |         1    |
| 72 |            733 | Hebbian        |             46 |           146 |         1    |
| 73 |            733 | Hebbian        |             55 |           146 |         0.91 |
| 74 |            733 | Hebbian        |             64 |           146 |         0.81 |
| 75 |            733 | Hebbian        |             74 |           146 |         0.56 |
| 76 |            733 | Hebbian        |             83 |           146 |         0.4  |
| 77 |            733 | Hebbian        |             92 |           146 |         0.18 |
| 78 |            733 | Hebbian        |            101 |           146 |         0.11 |
| 79 |            733 | Hebbian        |            111 |           146 |         0.01 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 80 |           1354 | Hebbian        |             46 |           270 |         1    |
| 81 |           1354 | Hebbian        |             62 |           270 |         1    |
| 82 |           1354 | Hebbian        |             78 |           270 |         0.96 |
| 83 |           1354 | Hebbian        |             93 |           270 |         0.9  |
| 84 |           1354 | Hebbian        |            109 |           270 |         0.72 |
| 85 |           1354 | Hebbian        |            125 |           270 |         0.5  |
| 86 |           1354 | Hebbian        |            140 |           270 |         0.33 |
| 87 |           1354 | Hebbian        |            156 |           270 |         0.13 |
| 88 |           1354 | Hebbian        |            172 |           270 |         0.03 |
| 89 |           1354 | Hebbian        |            187 |           270 |         0.01 |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 90 |           2500 | Hebbian        |             79 |           500 |         1    |
| 91 |           2500 | Hebbian        |            106 |           500 |         1    |
| 92 |           2500 | Hebbian        |            133 |           500 |         0.97 |
| 93 |           2500 | Hebbian        |            159 |           500 |         0.94 |
| 94 |           2500 | Hebbian        |            186 |           500 |         0.73 |
| 95 |           2500 | Hebbian        |            213 |           500 |         0.48 |
| 96 |           2500 | Hebbian        |            239 |           500 |         0.29 |
| 97 |           2500 | Hebbian        |            266 |           500 |         0.09 |
| 98 |           2500 | Hebbian        |            292 |           500 |         0.03 |
| 99 |           2500 | Hebbian        |            319 |           500 |         0    |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  0 |             10 | Storkey        |              2 |             2 |          0.9 |
|  1 |             10 | Storkey        |              3 |             2 |          0.8 |
|  2 |             10 | Storkey        |              3 |             2 |          0.8 |
|  3 |             10 | Storkey        |              4 |             2 |          0.6 |
|  4 |             10 | Storkey        |              5 |             2 |          0.4 |
|  5 |             10 | Storkey        |              6 |             2 |          0.5 |
|  6 |             10 | Storkey        |              6 |             2 |          0.4 |
|  7 |             10 | Storkey        |              7 |             2 |          0   |
|  8 |             10 | Storkey        |              8 |             2 |          0   |
|  9 |             10 | Storkey        |              9 |             2 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 10 |             18 | Storkey        |              3 |             3 |          1   |
| 11 |             18 | Storkey        |              4 |             3 |          0.6 |
| 12 |             18 | Storkey        |              6 |             3 |          1   |
| 13 |             18 | Storkey        |              7 |             3 |          0.6 |
| 14 |             18 | Storkey        |              8 |             3 |          0.3 |
| 15 |             18 | Storkey        |              9 |             3 |          0.5 |
| 16 |             18 | Storkey        |             11 |             3 |          0   |
| 17 |             18 | Storkey        |             12 |             3 |          0   |
| 18 |             18 | Storkey        |             13 |             3 |          0.1 |
| 19 |             18 | Storkey        |             14 |             3 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 20 |             34 | Storkey        |              6 |             6 |          1   |
| 21 |             34 | Storkey        |              8 |             6 |          0.6 |
| 22 |             34 | Storkey        |             10 |             6 |          0.6 |
| 23 |             34 | Storkey        |             12 |             6 |          1   |
| 24 |             34 | Storkey        |             14 |             6 |          0.7 |
| 25 |             34 | Storkey        |             17 |             6 |          0.3 |
| 26 |             34 | Storkey        |             19 |             6 |          0.2 |
| 27 |             34 | Storkey        |             21 |             6 |          0   |
| 28 |             34 | Storkey        |             23 |             6 |          0   |
| 29 |             34 | Storkey        |             25 |             6 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 30 |             63 | Storkey        |             10 |            12 |          1   |
| 31 |             63 | Storkey        |             14 |            12 |          1   |
| 32 |             63 | Storkey        |             18 |            12 |          0.7 |
| 33 |             63 | Storkey        |             21 |            12 |          0.5 |
| 34 |             63 | Storkey        |             25 |            12 |          0.3 |
| 35 |             63 | Storkey        |             29 |            12 |          0.2 |
| 36 |             63 | Storkey        |             32 |            12 |          0   |
| 37 |             63 | Storkey        |             36 |            12 |          0   |
| 38 |             63 | Storkey        |             40 |            12 |          0   |
| 39 |             63 | Storkey        |             43 |            12 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 40 |            116 | Storkey        |             18 |            23 |          1   |
| 41 |            116 | Storkey        |             25 |            23 |          1   |
| 42 |            116 | Storkey        |             31 |            23 |          1   |
| 43 |            116 | Storkey        |             37 |            23 |          0.5 |
| 44 |            116 | Storkey        |             43 |            23 |          0.1 |
| 45 |            116 | Storkey        |             50 |            23 |          0   |
| 46 |            116 | Storkey        |             56 |            23 |          0   |
| 47 |            116 | Storkey        |             62 |            23 |          0   |
| 48 |            116 | Storkey        |             68 |            23 |          0   |
| 49 |            116 | Storkey        |             75 |            23 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 50 |            215 | Storkey        |             32 |            43 |          1   |
| 51 |            215 | Storkey        |             43 |            43 |          1   |
| 52 |            215 | Storkey        |             54 |            43 |          1   |
| 53 |            215 | Storkey        |             65 |            43 |          0.2 |
| 54 |            215 | Storkey        |             76 |            43 |          0.1 |
| 55 |            215 | Storkey        |             87 |            43 |          0   |
| 56 |            215 | Storkey        |             98 |            43 |          0   |
| 57 |            215 | Storkey        |            109 |            43 |          0   |
| 58 |            215 | Storkey        |            120 |            43 |          0   |
| 59 |            215 | Storkey        |            131 |            43 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 60 |            397 | Storkey        |             57 |            79 |          1   |
| 61 |            397 | Storkey        |             76 |            79 |          1   |
| 62 |            397 | Storkey        |             95 |            79 |          1   |
| 63 |            397 | Storkey        |            114 |            79 |          0.9 |
| 64 |            397 | Storkey        |            133 |            79 |          0   |
| 65 |            397 | Storkey        |            153 |            79 |          0   |
| 66 |            397 | Storkey        |            172 |            79 |          0   |
| 67 |            397 | Storkey        |            191 |            79 |          0   |
| 68 |            397 | Storkey        |            210 |            79 |          0   |
| 69 |            397 | Storkey        |            229 |            79 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 70 |            733 | Storkey        |            100 |           146 |          1   |
| 71 |            733 | Storkey        |            134 |           146 |          1   |
| 72 |            733 | Storkey        |            168 |           146 |          1   |
| 73 |            733 | Storkey        |            201 |           146 |          0.9 |
| 74 |            733 | Storkey        |            235 |           146 |          0.4 |
| 75 |            733 | Storkey        |            269 |           146 |          0   |
| 76 |            733 | Storkey        |            302 |           146 |          0   |
| 77 |            733 | Storkey        |            336 |           146 |          0   |
| 78 |            733 | Storkey        |            369 |           146 |          0   |
| 79 |            733 | Storkey        |            403 |           146 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 80 |           1354 | Storkey        |            178 |           270 |          1   |
| 81 |           1354 | Storkey        |            237 |           270 |          1   |
| 82 |           1354 | Storkey        |            297 |           270 |          1   |
| 83 |           1354 | Storkey        |            356 |           270 |          0.6 |
| 84 |           1354 | Storkey        |            415 |           270 |          0   |
| 85 |           1354 | Storkey        |            475 |           270 |          0   |
| 86 |           1354 | Storkey        |            534 |           270 |          0   |
| 87 |           1354 | Storkey        |            594 |           270 |          0   |
| 88 |           1354 | Storkey        |            653 |           270 |          0   |
| 89 |           1354 | Storkey        |            713 |           270 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 90 |           2500 | Storkey        |            315 |           500 |          1   |
| 91 |           2500 | Storkey        |            421 |           500 |          1   |
| 92 |           2500 | Storkey        |            526 |           500 |          1   |
| 93 |           2500 | Storkey        |            631 |           500 |          0.7 |
| 94 |           2500 | Storkey        |            737 |           500 |          0   |
| 95 |           2500 | Storkey        |            842 |           500 |          0   |
| 96 |           2500 | Storkey        |            947 |           500 |          0   |
| 97 |           2500 | Storkey        |           1053 |           500 |          0   |
| 98 |           2500 | Storkey        |           1158 |           500 |          0   |
| 99 |           2500 | Storkey        |           1263 |           500 |          0   |

## Datas regarding the robustness


|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|   0 |             10 | Hebbian        |              2 |             2 |         0.84 |
|   1 |             10 | Hebbian        |              2 |             2 |         0.82 |
|   2 |             10 | Hebbian        |              2 |             3 |         0.55 |
|   3 |             10 | Hebbian        |              2 |             3 |         0.53 |
|   4 |             10 | Hebbian        |              2 |             4 |         0.2  |
|   5 |             10 | Hebbian        |              2 |             4 |         0.16 |
|   6 |             10 | Hebbian        |              2 |             5 |         0.04 |
|   7 |             10 | Hebbian        |              2 |             5 |         0.05 |
|   8 |             10 | Hebbian        |              2 |             6 |         0    |
|   9 |             10 | Hebbian        |              2 |             6 |         0    |
|  10 |             10 | Hebbian        |              2 |             7 |         0    |
|  11 |             10 | Hebbian        |              2 |             7 |         0    |
|  12 |             10 | Hebbian        |              2 |             8 |         0    |
|  13 |             10 | Hebbian        |              2 |             8 |         0    |
|  14 |             10 | Hebbian        |              2 |             9 |         0    |
|  15 |             10 | Hebbian        |              2 |             9 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  16 |             18 | Hebbian        |              2 |             3 |         0.99 |
|  17 |             18 | Hebbian        |              2 |             4 |         0.97 |
|  18 |             18 | Hebbian        |              2 |             5 |         0.85 |
|  19 |             18 | Hebbian        |              2 |             6 |         0.82 |
|  20 |             18 | Hebbian        |              2 |             7 |         0.53 |
|  21 |             18 | Hebbian        |              2 |             8 |         0.24 |
|  22 |             18 | Hebbian        |              2 |             9 |         0    |
|  23 |             18 | Hebbian        |              2 |             9 |         0.01 |
|  24 |             18 | Hebbian        |              2 |            10 |         0    |
|  25 |             18 | Hebbian        |              2 |            11 |         0    |
|  26 |             18 | Hebbian        |              2 |            12 |         0    |
|  27 |             18 | Hebbian        |              2 |            13 |         0    |
|  28 |             18 | Hebbian        |              2 |            14 |         0    |
|  29 |             18 | Hebbian        |              2 |            15 |         0    |
|  30 |             18 | Hebbian        |              2 |            16 |         0    |
|  31 |             18 | Hebbian        |              2 |            17 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  32 |             34 | Hebbian        |              2 |             6 |         1    |
|  33 |             34 | Hebbian        |              2 |             8 |         1    |
|  34 |             34 | Hebbian        |              2 |            10 |         0.98 |
|  35 |             34 | Hebbian        |              2 |            11 |         0.96 |
|  36 |             34 | Hebbian        |              2 |            13 |         0.74 |
|  37 |             34 | Hebbian        |              2 |            15 |         0.43 |
|  38 |             34 | Hebbian        |              2 |            17 |         0    |
|  39 |             34 | Hebbian        |              2 |            18 |         0    |
|  40 |             34 | Hebbian        |              2 |            20 |         0    |
|  41 |             34 | Hebbian        |              2 |            22 |         0    |
|  42 |             34 | Hebbian        |              2 |            23 |         0    |
|  43 |             34 | Hebbian        |              2 |            25 |         0    |
|  44 |             34 | Hebbian        |              2 |            27 |         0    |
|  45 |             34 | Hebbian        |              2 |            28 |         0    |
|  46 |             34 | Hebbian        |              2 |            30 |         0    |
|  47 |             34 | Hebbian        |              2 |            32 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  48 |             63 | Hebbian        |              2 |            12 |         1    |
|  49 |             63 | Hebbian        |              2 |            15 |         1    |
|  50 |             63 | Hebbian        |              2 |            18 |         1    |
|  51 |             63 | Hebbian        |              2 |            22 |         1    |
|  52 |             63 | Hebbian        |              2 |            25 |         0.83 |
|  53 |             63 | Hebbian        |              2 |            28 |         0.5  |
|  54 |             63 | Hebbian        |              2 |            31 |         0    |
|  55 |             63 | Hebbian        |              2 |            34 |         0    |
|  56 |             63 | Hebbian        |              2 |            37 |         0    |
|  57 |             63 | Hebbian        |              2 |            40 |         0    |
|  58 |             63 | Hebbian        |              2 |            44 |         0    |
|  59 |             63 | Hebbian        |              2 |            47 |         0    |
|  60 |             63 | Hebbian        |              2 |            50 |         0    |
|  61 |             63 | Hebbian        |              2 |            53 |         0    |
|  62 |             63 | Hebbian        |              2 |            56 |         0    |
|  63 |             63 | Hebbian        |              2 |            59 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  64 |            116 | Hebbian        |              2 |            23 |         1    |
|  65 |            116 | Hebbian        |              2 |            29 |         1    |
|  66 |            116 | Hebbian        |              2 |            34 |         1    |
|  67 |            116 | Hebbian        |              2 |            40 |         1    |
|  68 |            116 | Hebbian        |              2 |            46 |         0.96 |
|  69 |            116 | Hebbian        |              2 |            52 |         0.67 |
|  70 |            116 | Hebbian        |              2 |            58 |         0    |
|  71 |            116 | Hebbian        |              2 |            63 |         0    |
|  72 |            116 | Hebbian        |              2 |            69 |         0    |
|  73 |            116 | Hebbian        |              2 |            75 |         0    |
|  74 |            116 | Hebbian        |              2 |            81 |         0    |
|  75 |            116 | Hebbian        |              2 |            87 |         0    |
|  76 |            116 | Hebbian        |              2 |            92 |         0    |
|  77 |            116 | Hebbian        |              2 |            98 |         0    |
|  78 |            116 | Hebbian        |              2 |           104 |         0    |
|  79 |            116 | Hebbian        |              2 |           110 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  80 |            215 | Hebbian        |              2 |            43 |         1    |
|  81 |            215 | Hebbian        |              2 |            53 |         1    |
|  82 |            215 | Hebbian        |              2 |            64 |         1    |
|  83 |            215 | Hebbian        |              2 |            75 |         1    |
|  84 |            215 | Hebbian        |              2 |            86 |         1    |
|  85 |            215 | Hebbian        |              2 |            96 |         0.91 |
|  86 |            215 | Hebbian        |              2 |           107 |         0    |
|  87 |            215 | Hebbian        |              2 |           118 |         0    |
|  88 |            215 | Hebbian        |              2 |           129 |         0    |
|  89 |            215 | Hebbian        |              2 |           139 |         0    |
|  90 |            215 | Hebbian        |              2 |           150 |         0    |
|  91 |            215 | Hebbian        |              2 |           161 |         0    |
|  92 |            215 | Hebbian        |              2 |           172 |         0    |
|  93 |            215 | Hebbian        |              2 |           182 |         0    |
|  94 |            215 | Hebbian        |              2 |           193 |         0    |
|  95 |            215 | Hebbian        |              2 |           204 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  96 |            397 | Hebbian        |              2 |            79 |         1    |
|  97 |            397 | Hebbian        |              2 |            99 |         1    |
|  98 |            397 | Hebbian        |              2 |           119 |         1    |
|  99 |            397 | Hebbian        |              2 |           138 |         1    |
| 100 |            397 | Hebbian        |              2 |           158 |         1    |
| 101 |            397 | Hebbian        |              2 |           178 |         0.94 |
| 102 |            397 | Hebbian        |              2 |           198 |         0    |
| 103 |            397 | Hebbian        |              2 |           218 |         0    |
| 104 |            397 | Hebbian        |              2 |           238 |         0    |
| 105 |            397 | Hebbian        |              2 |           258 |         0    |
| 106 |            397 | Hebbian        |              2 |           277 |         0    |
| 107 |            397 | Hebbian        |              2 |           297 |         0    |
| 108 |            397 | Hebbian        |              2 |           317 |         0    |
| 109 |            397 | Hebbian        |              2 |           337 |         0    |
| 110 |            397 | Hebbian        |              2 |           357 |         0    |
| 111 |            397 | Hebbian        |              2 |           377 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 112 |            733 | Hebbian        |              2 |           146 |         1    |
| 113 |            733 | Hebbian        |              2 |           183 |         1    |
| 114 |            733 | Hebbian        |              2 |           219 |         1    |
| 115 |            733 | Hebbian        |              2 |           256 |         1    |
| 116 |            733 | Hebbian        |              2 |           293 |         1    |
| 117 |            733 | Hebbian        |              2 |           329 |         0.99 |
| 118 |            733 | Hebbian        |              2 |           366 |         0    |
| 119 |            733 | Hebbian        |              2 |           403 |         0    |
| 120 |            733 | Hebbian        |              2 |           439 |         0    |
| 121 |            733 | Hebbian        |              2 |           476 |         0    |
| 122 |            733 | Hebbian        |              2 |           513 |         0    |
| 123 |            733 | Hebbian        |              2 |           549 |         0    |
| 124 |            733 | Hebbian        |              2 |           586 |         0    |
| 125 |            733 | Hebbian        |              2 |           623 |         0    |
| 126 |            733 | Hebbian        |              2 |           659 |         0    |
| 127 |            733 | Hebbian        |              2 |           696 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 128 |           1354 | Hebbian        |              2 |           270 |         1    |
| 129 |           1354 | Hebbian        |              2 |           338 |         1    |
| 130 |           1354 | Hebbian        |              2 |           406 |         1    |
| 131 |           1354 | Hebbian        |              2 |           473 |         1    |
| 132 |           1354 | Hebbian        |              2 |           541 |         1    |
| 133 |           1354 | Hebbian        |              2 |           609 |         1    |
| 134 |           1354 | Hebbian        |              2 |           677 |         0    |
| 135 |           1354 | Hebbian        |              2 |           744 |         0    |
| 136 |           1354 | Hebbian        |              2 |           812 |         0    |
| 137 |           1354 | Hebbian        |              2 |           880 |         0    |
| 138 |           1354 | Hebbian        |              2 |           947 |         0    |
| 139 |           1354 | Hebbian        |              2 |          1015 |         0    |
| 140 |           1354 | Hebbian        |              2 |          1083 |         0    |
| 141 |           1354 | Hebbian        |              2 |          1150 |         0    |
| 142 |           1354 | Hebbian        |              2 |          1218 |         0    |
| 143 |           1354 | Hebbian        |              2 |          1286 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 144 |           2500 | Hebbian        |              2 |           500 |         1    |
| 145 |           2500 | Hebbian        |              2 |           625 |         1    |
| 146 |           2500 | Hebbian        |              2 |           750 |         1    |
| 147 |           2500 | Hebbian        |              2 |           875 |         1    |
| 148 |           2500 | Hebbian        |              2 |          1000 |         1    |
| 149 |           2500 | Hebbian        |              2 |          1125 |         1    |
| 150 |           2500 | Hebbian        |              2 |          1250 |         0    |
| 151 |           2500 | Hebbian        |              2 |          1375 |         0    |
| 152 |           2500 | Hebbian        |              2 |          1500 |         0    |
| 153 |           2500 | Hebbian        |              2 |          1625 |         0    |
| 154 |           2500 | Hebbian        |              2 |          1750 |         0    |
| 155 |           2500 | Hebbian        |              2 |          1875 |         0    |
| 156 |           2500 | Hebbian        |              2 |          2000 |         0    |
| 157 |           2500 | Hebbian        |              2 |          2125 |         0    |
| 158 |           2500 | Hebbian        |              2 |          2250 |         0    |
| 159 |           2500 | Hebbian        |              2 |          2375 |         0    |

|     |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|----:|---------------:|:---------------|---------------:|--------------:|-------------:|
|   0 |             10 | Storkey        |              2 |             2 |          1   |
|   1 |             10 | Storkey        |              2 |             2 |          1   |
|   2 |             10 | Storkey        |              2 |             3 |          0.4 |
|   3 |             10 | Storkey        |              2 |             3 |          0.8 |
|   4 |             10 | Storkey        |              2 |             4 |          0.2 |
|   5 |             10 | Storkey        |              2 |             4 |          0   |
|   6 |             10 | Storkey        |              2 |             5 |          0   |
|   7 |             10 | Storkey        |              2 |             5 |          0   |
|   8 |             10 | Storkey        |              2 |             6 |          0   |
|   9 |             10 | Storkey        |              2 |             6 |          0   |
|  10 |             10 | Storkey        |              2 |             7 |          0   |
|  11 |             10 | Storkey        |              2 |             7 |          0   |
|  12 |             10 | Storkey        |              2 |             8 |          0   |
|  13 |             10 | Storkey        |              2 |             8 |          0   |
|  14 |             10 | Storkey        |              2 |             9 |          0   |
|  15 |             10 | Storkey        |              2 |             9 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  16 |             18 | Storkey        |              2 |             3 |          1   |
|  17 |             18 | Storkey        |              2 |             4 |          1   |
|  18 |             18 | Storkey        |              2 |             5 |          1   |
|  19 |             18 | Storkey        |              2 |             6 |          0.7 |
|  20 |             18 | Storkey        |              2 |             7 |          0.9 |
|  21 |             18 | Storkey        |              2 |             8 |          0.3 |
|  22 |             18 | Storkey        |              2 |             9 |          0   |
|  23 |             18 | Storkey        |              2 |             9 |          0   |
|  24 |             18 | Storkey        |              2 |            10 |          0   |
|  25 |             18 | Storkey        |              2 |            11 |          0   |
|  26 |             18 | Storkey        |              2 |            12 |          0   |
|  27 |             18 | Storkey        |              2 |            13 |          0   |
|  28 |             18 | Storkey        |              2 |            14 |          0   |
|  29 |             18 | Storkey        |              2 |            15 |          0   |
|  30 |             18 | Storkey        |              2 |            16 |          0   |
|  31 |             18 | Storkey        |              2 |            17 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  32 |             34 | Storkey        |              2 |             6 |          1   |
|  33 |             34 | Storkey        |              2 |             8 |          1   |
|  34 |             34 | Storkey        |              2 |            10 |          1   |
|  35 |             34 | Storkey        |              2 |            11 |          1   |
|  36 |             34 | Storkey        |              2 |            13 |          0.7 |
|  37 |             34 | Storkey        |              2 |            15 |          0.5 |
|  38 |             34 | Storkey        |              2 |            17 |          0   |
|  39 |             34 | Storkey        |              2 |            18 |          0   |
|  40 |             34 | Storkey        |              2 |            20 |          0   |
|  41 |             34 | Storkey        |              2 |            22 |          0   |
|  42 |             34 | Storkey        |              2 |            23 |          0   |
|  43 |             34 | Storkey        |              2 |            25 |          0   |
|  44 |             34 | Storkey        |              2 |            27 |          0   |
|  45 |             34 | Storkey        |              2 |            28 |          0   |
|  46 |             34 | Storkey        |              2 |            30 |          0   |
|  47 |             34 | Storkey        |              2 |            32 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  48 |             63 | Storkey        |              2 |            12 |          1   |
|  49 |             63 | Storkey        |              2 |            15 |          1   |
|  50 |             63 | Storkey        |              2 |            18 |          1   |
|  51 |             63 | Storkey        |              2 |            22 |          1   |
|  52 |             63 | Storkey        |              2 |            25 |          0.9 |
|  53 |             63 | Storkey        |              2 |            28 |          0.4 |
|  54 |             63 | Storkey        |              2 |            31 |          0   |
|  55 |             63 | Storkey        |              2 |            34 |          0   |
|  56 |             63 | Storkey        |              2 |            37 |          0   |
|  57 |             63 | Storkey        |              2 |            40 |          0   |
|  58 |             63 | Storkey        |              2 |            44 |          0   |
|  59 |             63 | Storkey        |              2 |            47 |          0   |
|  60 |             63 | Storkey        |              2 |            50 |          0   |
|  61 |             63 | Storkey        |              2 |            53 |          0   |
|  62 |             63 | Storkey        |              2 |            56 |          0   |
|  63 |             63 | Storkey        |              2 |            59 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  64 |            116 | Storkey        |              2 |            23 |          1   |
|  65 |            116 | Storkey        |              2 |            29 |          1   |
|  66 |            116 | Storkey        |              2 |            34 |          1   |
|  67 |            116 | Storkey        |              2 |            40 |          1   |
|  68 |            116 | Storkey        |              2 |            46 |          0.9 |
|  69 |            116 | Storkey        |              2 |            52 |          0.7 |
|  70 |            116 | Storkey        |              2 |            58 |          0   |
|  71 |            116 | Storkey        |              2 |            63 |          0   |
|  72 |            116 | Storkey        |              2 |            69 |          0   |
|  73 |            116 | Storkey        |              2 |            75 |          0   |
|  74 |            116 | Storkey        |              2 |            81 |          0   |
|  75 |            116 | Storkey        |              2 |            87 |          0   |
|  76 |            116 | Storkey        |              2 |            92 |          0   |
|  77 |            116 | Storkey        |              2 |            98 |          0   |
|  78 |            116 | Storkey        |              2 |           104 |          0   |
|  79 |            116 | Storkey        |              2 |           110 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  80 |            215 | Storkey        |              2 |            43 |          1   |
|  81 |            215 | Storkey        |              2 |            53 |          1   |
|  82 |            215 | Storkey        |              2 |            64 |          1   |
|  83 |            215 | Storkey        |              2 |            75 |          1   |
|  84 |            215 | Storkey        |              2 |            86 |          1   |
|  85 |            215 | Storkey        |              2 |            96 |          0.7 |
|  86 |            215 | Storkey        |              2 |           107 |          0   |
|  87 |            215 | Storkey        |              2 |           118 |          0   |
|  88 |            215 | Storkey        |              2 |           129 |          0   |
|  89 |            215 | Storkey        |              2 |           139 |          0   |
|  90 |            215 | Storkey        |              2 |           150 |          0   |
|  91 |            215 | Storkey        |              2 |           161 |          0   |
|  92 |            215 | Storkey        |              2 |           172 |          0   |
|  93 |            215 | Storkey        |              2 |           182 |          0   |
|  94 |            215 | Storkey        |              2 |           193 |          0   |
|  95 |            215 | Storkey        |              2 |           204 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
|  96 |            397 | Storkey        |              2 |            79 |          1   |
|  97 |            397 | Storkey        |              2 |            99 |          1   |
|  98 |            397 | Storkey        |              2 |           119 |          1   |
|  99 |            397 | Storkey        |              2 |           138 |          1   |
| 100 |            397 | Storkey        |              2 |           158 |          1   |
| 101 |            397 | Storkey        |              2 |           178 |          0.9 |
| 102 |            397 | Storkey        |              2 |           198 |          0   |
| 103 |            397 | Storkey        |              2 |           218 |          0   |
| 104 |            397 | Storkey        |              2 |           238 |          0   |
| 105 |            397 | Storkey        |              2 |           258 |          0   |
| 106 |            397 | Storkey        |              2 |           277 |          0   |
| 107 |            397 | Storkey        |              2 |           297 |          0   |
| 108 |            397 | Storkey        |              2 |           317 |          0   |
| 109 |            397 | Storkey        |              2 |           337 |          0   |
| 110 |            397 | Storkey        |              2 |           357 |          0   |
| 111 |            397 | Storkey        |              2 |           377 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 112 |            733 | Storkey        |              2 |           146 |          1   |
| 113 |            733 | Storkey        |              2 |           183 |          1   |
| 114 |            733 | Storkey        |              2 |           219 |          1   |
| 115 |            733 | Storkey        |              2 |           256 |          1   |
| 116 |            733 | Storkey        |              2 |           293 |          1   |
| 117 |            733 | Storkey        |              2 |           329 |          1   |
| 118 |            733 | Storkey        |              2 |           366 |          0   |
| 119 |            733 | Storkey        |              2 |           403 |          0   |
| 120 |            733 | Storkey        |              2 |           439 |          0   |
| 121 |            733 | Storkey        |              2 |           476 |          0   |
| 122 |            733 | Storkey        |              2 |           513 |          0   |
| 123 |            733 | Storkey        |              2 |           549 |          0   |
| 124 |            733 | Storkey        |              2 |           586 |          0   |
| 125 |            733 | Storkey        |              2 |           623 |          0   |
| 126 |            733 | Storkey        |              2 |           659 |          0   |
| 127 |            733 | Storkey        |              2 |           696 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 128 |           1354 | Storkey        |              2 |           270 |          1   |
| 129 |           1354 | Storkey        |              2 |           338 |          1   |
| 130 |           1354 | Storkey        |              2 |           406 |          1   |
| 131 |           1354 | Storkey        |              2 |           473 |          1   |
| 132 |           1354 | Storkey        |              2 |           541 |          1   |
| 133 |           1354 | Storkey        |              2 |           609 |          1   |
| 134 |           1354 | Storkey        |              2 |           677 |          0   |
| 135 |           1354 | Storkey        |              2 |           744 |          0   |
| 136 |           1354 | Storkey        |              2 |           812 |          0   |
| 137 |           1354 | Storkey        |              2 |           880 |          0   |
| 138 |           1354 | Storkey        |              2 |           947 |          0   |
| 139 |           1354 | Storkey        |              2 |          1015 |          0   |
| 140 |           1354 | Storkey        |              2 |          1083 |          0   |
| 141 |           1354 | Storkey        |              2 |          1150 |          0   |
| 142 |           1354 | Storkey        |              2 |          1218 |          0   |
| 143 |           1354 | Storkey        |              2 |          1286 |          0   |

|    |   network size | weight_rule    |   num_patterns |   num_perturb |   match_frac |
|---:|---------------:|:---------------|---------------:|--------------:|-------------:|
| 144 |           2500 | Storkey        |              2 |           500 |          1   |
| 145 |           2500 | Storkey        |              2 |           625 |          1   |
| 146 |           2500 | Storkey        |              2 |           750 |          1   |
| 147 |           2500 | Storkey        |              2 |           875 |          1   |
| 148 |           2500 | Storkey        |              2 |          1000 |          1   |
| 149 |           2500 | Storkey        |              2 |          1125 |          1   |
| 150 |           2500 | Storkey        |              2 |          1250 |          0   |
| 151 |           2500 | Storkey        |              2 |          1375 |          0   |
| 152 |           2500 | Storkey        |              2 |          1500 |          0   |
| 153 |           2500 | Storkey        |              2 |          1625 |          0   |
| 154 |           2500 | Storkey        |              2 |          1750 |          0   |
| 155 |           2500 | Storkey        |              2 |          1875 |          0   |
| 156 |           2500 | Storkey        |              2 |          2000 |          0   |
| 157 |           2500 | Storkey        |              2 |          2125 |          0   |
| 158 |           2500 | Storkey        |              2 |          2250 |          0   |
| 159 |           2500 | Storkey        |              2 |          2375 |          0   |


