{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO0ezZ3+bAkpoI60RfaFNod",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/marypeterdan/agentic_ai_samples/blob/main/pdfreader.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yh5qL0I-B8es",
        "outputId": "55ed1bae-e2d5-4553-ac23-a743497198c0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: sentence-transformers in /usr/local/lib/python3.11/dist-packages (3.4.1)\n",
            "Collecting faiss-cpu\n",
            "  Downloading faiss_cpu-1.10.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (4.4 kB)\n",
            "Collecting PyPDF2\n",
            "  Downloading pypdf2-3.0.1-py3-none-any.whl.metadata (6.8 kB)\n",
            "Requirement already satisfied: langchain in /usr/local/lib/python3.11/dist-packages (0.3.21)\n",
            "Requirement already satisfied: transformers in /usr/local/lib/python3.11/dist-packages (4.50.2)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (4.67.1)\n",
            "Requirement already satisfied: torch>=1.11.0 in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (2.6.0+cu124)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (1.6.1)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (1.14.1)\n",
            "Requirement already satisfied: huggingface-hub>=0.20.0 in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (0.29.3)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (11.1.0)\n",
            "Requirement already satisfied: numpy<3.0,>=1.25.0 in /usr/local/lib/python3.11/dist-packages (from faiss-cpu) (2.0.2)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from faiss-cpu) (24.2)\n",
            "Requirement already satisfied: langchain-core<1.0.0,>=0.3.45 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.49)\n",
            "Requirement already satisfied: langchain-text-splitters<1.0.0,>=0.3.7 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.7)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.17 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.19)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.11.0)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.0.40)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.32.3)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain) (6.0.2)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from transformers) (3.18.0)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.11/dist-packages (from transformers) (2024.11.6)\n",
            "Requirement already satisfied: tokenizers<0.22,>=0.21 in /usr/local/lib/python3.11/dist-packages (from transformers) (0.21.1)\n",
            "Requirement already satisfied: safetensors>=0.4.3 in /usr/local/lib/python3.11/dist-packages (from transformers) (0.5.3)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers) (2025.3.0)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers) (4.13.0)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.45->langchain) (9.0.0)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.45->langchain) (1.33)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (0.28.1)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (3.10.16)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (0.23.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.33.0)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.4.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (2025.1.31)\n",
            "Requirement already satisfied: greenlet>=1 in /usr/local/lib/python3.11/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (3.1.1)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (3.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (3.1.6)\n",
            "Collecting nvidia-cuda-nvrtc-cu12==12.4.127 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cuda-runtime-cu12==12.4.127 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cuda-cupti-cu12==12.4.127 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cuda_cupti_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Collecting nvidia-cudnn-cu12==9.1.0.70 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Collecting nvidia-cublas-cu12==12.4.5.8 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cufft-cu12==11.2.1.3 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-curand-cu12==10.3.5.147 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Collecting nvidia-cusolver-cu12==11.6.1.9 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Collecting nvidia-cusparse-cu12==12.3.1.170 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)\n",
            "Requirement already satisfied: nvidia-cusparselt-cu12==0.6.2 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (0.6.2)\n",
            "Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (2.21.5)\n",
            "Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.4.127)\n",
            "Collecting nvidia-nvjitlink-cu12==12.4.127 (from torch>=1.11.0->sentence-transformers)\n",
            "  Downloading nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: triton==3.2.0 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (3.2.0)\n",
            "Requirement already satisfied: sympy==1.13.1 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (1.13.1)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from sympy==1.13.1->torch>=1.11.0->sentence-transformers) (1.3.0)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn->sentence-transformers) (1.4.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn->sentence-transformers) (3.6.0)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (4.9.0)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (0.14.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<1.0.0,>=0.3.45->langchain) (3.0.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->torch>=1.11.0->sentence-transformers) (3.0.2)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (1.3.1)\n",
            "Downloading faiss_cpu-1.10.0-cp311-cp311-manylinux_2_28_x86_64.whl (30.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m30.7/30.7 MB\u001b[0m \u001b[31m41.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pypdf2-3.0.1-py3-none-any.whl (232 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m232.6/232.6 kB\u001b[0m \u001b[31m11.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl (363.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m363.4/363.4 MB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cuda_cupti_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (13.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m13.8/13.8 MB\u001b[0m \u001b[31m48.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (24.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m24.6/24.6 MB\u001b[0m \u001b[31m42.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (883 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m883.7/883.7 kB\u001b[0m \u001b[31m33.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl (664.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m664.8/664.8 MB\u001b[0m \u001b[31m2.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl (211.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m211.5/211.5 MB\u001b[0m \u001b[31m5.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl (56.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m56.3/56.3 MB\u001b[0m \u001b[31m11.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl (127.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m127.9/127.9 MB\u001b[0m \u001b[31m7.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl (207.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.5/207.5 MB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (21.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m21.1/21.1 MB\u001b[0m \u001b[31m69.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: PyPDF2, nvidia-nvjitlink-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, faiss-cpu, nvidia-cusparse-cu12, nvidia-cudnn-cu12, nvidia-cusolver-cu12\n",
            "  Attempting uninstall: nvidia-nvjitlink-cu12\n",
            "    Found existing installation: nvidia-nvjitlink-cu12 12.5.82\n",
            "    Uninstalling nvidia-nvjitlink-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-nvjitlink-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-curand-cu12\n",
            "    Found existing installation: nvidia-curand-cu12 10.3.6.82\n",
            "    Uninstalling nvidia-curand-cu12-10.3.6.82:\n",
            "      Successfully uninstalled nvidia-curand-cu12-10.3.6.82\n",
            "  Attempting uninstall: nvidia-cufft-cu12\n",
            "    Found existing installation: nvidia-cufft-cu12 11.2.3.61\n",
            "    Uninstalling nvidia-cufft-cu12-11.2.3.61:\n",
            "      Successfully uninstalled nvidia-cufft-cu12-11.2.3.61\n",
            "  Attempting uninstall: nvidia-cuda-runtime-cu12\n",
            "    Found existing installation: nvidia-cuda-runtime-cu12 12.5.82\n",
            "    Uninstalling nvidia-cuda-runtime-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-cuda-runtime-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-cuda-nvrtc-cu12\n",
            "    Found existing installation: nvidia-cuda-nvrtc-cu12 12.5.82\n",
            "    Uninstalling nvidia-cuda-nvrtc-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-cuda-nvrtc-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-cuda-cupti-cu12\n",
            "    Found existing installation: nvidia-cuda-cupti-cu12 12.5.82\n",
            "    Uninstalling nvidia-cuda-cupti-cu12-12.5.82:\n",
            "      Successfully uninstalled nvidia-cuda-cupti-cu12-12.5.82\n",
            "  Attempting uninstall: nvidia-cublas-cu12\n",
            "    Found existing installation: nvidia-cublas-cu12 12.5.3.2\n",
            "    Uninstalling nvidia-cublas-cu12-12.5.3.2:\n",
            "      Successfully uninstalled nvidia-cublas-cu12-12.5.3.2\n",
            "  Attempting uninstall: nvidia-cusparse-cu12\n",
            "    Found existing installation: nvidia-cusparse-cu12 12.5.1.3\n",
            "    Uninstalling nvidia-cusparse-cu12-12.5.1.3:\n",
            "      Successfully uninstalled nvidia-cusparse-cu12-12.5.1.3\n",
            "  Attempting uninstall: nvidia-cudnn-cu12\n",
            "    Found existing installation: nvidia-cudnn-cu12 9.3.0.75\n",
            "    Uninstalling nvidia-cudnn-cu12-9.3.0.75:\n",
            "      Successfully uninstalled nvidia-cudnn-cu12-9.3.0.75\n",
            "  Attempting uninstall: nvidia-cusolver-cu12\n",
            "    Found existing installation: nvidia-cusolver-cu12 11.6.3.83\n",
            "    Uninstalling nvidia-cusolver-cu12-11.6.3.83:\n",
            "      Successfully uninstalled nvidia-cusolver-cu12-11.6.3.83\n",
            "Successfully installed PyPDF2-3.0.1 faiss-cpu-1.10.0 nvidia-cublas-cu12-12.4.5.8 nvidia-cuda-cupti-cu12-12.4.127 nvidia-cuda-nvrtc-cu12-12.4.127 nvidia-cuda-runtime-cu12-12.4.127 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nvjitlink-cu12-12.4.127\n"
          ]
        }
      ],
      "source": [
        "!pip install sentence-transformers faiss-cpu PyPDF2 langchain transformers\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import faiss\n",
        "import numpy as np\n",
        "from PyPDF2 import PdfReader\n",
        "from sentence_transformers import SentenceTransformer\n",
        "from langchain.text_splitter import CharacterTextSplitter\n",
        "from transformers import pipeline"
      ],
      "metadata": {
        "id": "3ze4U-VhCs1Q"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Step 1: Load PDF and extract text\n",
        "def load_pdf(pdf_path):\n",
        "    pdf = PdfReader(pdf_path)\n",
        "    text = \"\"\n",
        "    for page in pdf.pages:\n",
        "        text += page.extract_text()\n",
        "    return text\n",
        "\n",
        "pdf_path = \"/content/aiadoption.pdf\"  # 👉 Change to your PDF path\n",
        "raw_text = load_pdf(pdf_path)\n",
        "\n",
        "# Step 2: Split text into chunks\n",
        "text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)\n",
        "docs = text_splitter.split_text(raw_text)\n",
        "\n",
        "# Step 3: Create embeddings using HuggingFace (local and free)\n",
        "model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # small & fast model\n",
        "\n",
        "embeddings = model.encode(docs)\n",
        "\n",
        "# Step 4: Store embeddings in FAISS\n",
        "dimension = embeddings.shape[1]\n",
        "index = faiss.IndexFlatL2(dimension)\n",
        "index.add(np.array(embeddings))\n",
        "\n",
        "# Step 5: Setup a QA pipeline for answering questions (using a local Hugging Face model)\n",
        "qa_pipeline = pipeline(\"question-answering\", model=\"distilbert-base-cased-distilled-squad\")\n",
        "\n",
        "# Step 6: Function to get the most relevant chunk & answer\n",
        "def get_answer(question):\n",
        "    # Convert question to embedding\n",
        "    question_embedding = model.encode([question])\n",
        "\n",
        "    # Search for most similar chunk in FAISS\n",
        "    distances, indices = index.search(np.array(question_embedding), k=1)\n",
        "    context = docs[indices[0][0]]\n",
        "\n",
        "    # Use QA model to answer based on that context\n",
        "    result = qa_pipeline(question=question, context=context)\n",
        "    return result['answer']\n",
        "\n",
        "# Example Question\n",
        "question = \"What is a microservice?\"\n",
        "answer = get_answer(question)\n",
        "print(f\"Question: {question}\")\n",
        "print(f\"Answer: {answer}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KZ5FqhNeDfeA",
        "outputId": "0d32e59b-7bcc-4b7b-962a-98f25b302056"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Device set to use cpu\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Question: What is a microservice?\n",
            "Answer: Service Discovery\n"
          ]
        }
      ]
    }
  ]
}