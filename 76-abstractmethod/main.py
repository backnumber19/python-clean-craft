from abc import ABC, abstractmethod
from typing import Dict, Any


class ModelConfig(ABC):
    """Abstract base class for model configurations"""

    def __init__(self, seq_len: int, pred_len: int, d_model: int):
        self.seq_len = seq_len
        self.pred_len = pred_len
        self.d_model = d_model

    @abstractmethod
    def get_search_space(self) -> Dict[str, Any]:
        """Define hyperparameter search space for optimization"""
        pass

    @abstractmethod
    def get_default_params(self) -> Dict[str, Any]:
        """Get default model parameters"""
        pass

    def validate_config(self) -> bool:
        """Common validation for all model configs"""
        return (
            self.seq_len > 0
            and self.pred_len > 0
            and self.d_model > 0
            and self.d_model % 8 == 0
        )


class CrossLinearConfig(ModelConfig):
    """Configuration for CrossLinear model"""

    def get_search_space(self) -> Dict[str, Any]:
        return {
            "learning_rate": [1e-5, 1e-3],
            "batch_size": [16, 32, 64, 128],
            "patch_len": [8, 16, 24, 32],
            "d_ff": [256, 512, 1024, 2048],
            "alpha": [0.1, 0.3, 0.5, 0.7, 0.9],
            "beta": [0.1, 0.3, 0.5, 0.7, 0.9],
            "dec_in": [7, 21, 321, 862],
        }

    def get_default_params(self) -> Dict[str, Any]:
        return {
            "model_type": "CrossLinear",
            "seq_len": self.seq_len,
            "pred_len": self.pred_len,
            "d_model": self.d_model,
            "task_name": "long_term_forecast",
            "features": "M",
        }


class CMoSConfig(ModelConfig):
    """Configuration for CMoS (Chunk-wise Spatial Correlations) model"""

    def get_search_space(self) -> Dict[str, Any]:
        return {
            "lr": [1e-5, 1e-3],
            "batch_size": [32, 64, 128, 256],
            "seg_size": [12, 24, 48, 96],
            "num_map": [2, 4, 8, 16],
            "conv_stride": [2, 4, 8],
            "dropout": [0.01, 0.05, 0.1, 0.2],
            "topk": [-1, 1, 2, 4],
            "use_pi": [True, False],
            "gamma": [0.5, 0.75, 0.9],
        }

    def get_default_params(self) -> Dict[str, Any]:
        return {
            "model_type": "CMoS",
            "seq_len": self.seq_len,
            "pred_len": self.pred_len,
            "d_model": self.d_model,
        }


def get_model_config(
    model_name: str, seq_len: int, pred_len: int, d_model: int
) -> ModelConfig:
    """Factory function to create appropriate model configuration"""
    if model_name.lower() == "crosslinear":
        return CrossLinearConfig(seq_len, pred_len, d_model)
    elif model_name.lower() == "cmos":
        return CMoSConfig(seq_len, pred_len, d_model)
    else:
        raise ValueError(f"Unsupported model type: {model_name}")


if __name__ == "__main__":
    config = get_model_config("crosslinear", seq_len=96, pred_len=24, d_model=512)

    if config.validate_config():
        search_space = config.get_search_space()
        default_params = config.get_default_params()
        print(f"Model: {default_params['model_type']}")
        print(f"Search space keys: {list(search_space.keys())}")

    # abstract_config = ModelConfig(96, 24, 512) # TypeError!
    # config = get_model_config('InvalidModel', 96, 24, 512) # ValueError!
