from setuptools import setup
import complex_model
import oasislmf.utils 

setup(
    name='OasisLMF_ComplexModelExample',
    version='1.0.0.0',
    entry_points={
        'console_scripts': [
            'OasisLMF_ComplexModelExample_gulcalc=complex_model.OasisLMF_ComplexModelExample_gulcalc:main'
        ]
    }
)
