## Case #76 - [Python] @abstractmethod

> 🧩 Reference: [LinkedIn Post](https://www.linkedin.com/posts/backnumber19lim_python-abstractmethod-hpo-activity-7367722805615869954-zKUK?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC4i7ZsBMeUAH3UpBvhusYv1qkmTlPJ4E6E)  

The @abstractmethod decorator is provided by Python's ABC (Abstract Base Classes) module and is extremely useful for systematically managing configurations of multiple models during hyperparameter optimization (HPO). While each model has different hyperparameter structures, enforcing a common interface allows consistent processing in HPO pipelines.

The code below demonstrates how to manage configurations for modern time series forecasting models like CrossLinear (refer to Case #71, #72) and CMoS (ICML '25) using @abstractmethod for unified management.

1️⃣ Abstract Config Base

The ModelConfig class inherits from ABC and declares get_search_space() and get_default_params() methods as abstract using @abstractmethod. It defines common attributes like seq_len, pred_len, and d_model that all configs should have, and provides common validation logic through the validate_config() method.

2️⃣ Model-specific Configs

CrossLinearConfig and CMoSConfig define hyperparameters specific to each model. CrossLinear includes parameters necessary for patch embedding-based architecture, while CMoS includes settings required for chunk-wise spatial correlation modeling.

3️⃣ Factory Pattern

The get_model_config() function creates appropriate config objects based on model names. HPO frameworks (Optuna, Ray Tune, etc.) can dynamically create configs and retrieve search spaces through this function, making it very convenient.

✅ The biggest advantage of this pattern is the ability to extend the system by adding new models without modifying existing HPO pipelines at all. Even when each model has different hyperparameters, they can be processed through the same interface, making experimental code very clean.