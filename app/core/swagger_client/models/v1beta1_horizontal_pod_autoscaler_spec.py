# coding: utf-8

"""
    

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1beta1HorizontalPodAutoscalerSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, scale_ref=None, max_replicas=None, min_replicas=None, cpu_utilization=None):
        """
        V1beta1HorizontalPodAutoscalerSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'scale_ref': 'V1beta1SubresourceReference',
            'max_replicas': 'int',
            'min_replicas': 'int',
            'cpu_utilization': 'V1beta1CPUTargetUtilization'
        }

        self.attribute_map = {
            'scale_ref': 'scaleRef',
            'max_replicas': 'maxReplicas',
            'min_replicas': 'minReplicas',
            'cpu_utilization': 'cpuUtilization'
        }

        self._scale_ref = scale_ref
        self._max_replicas = max_replicas
        self._min_replicas = min_replicas
        self._cpu_utilization = cpu_utilization

    @property
    def scale_ref(self):
        """
        Gets the scale_ref of this V1beta1HorizontalPodAutoscalerSpec.
        reference to Scale subresource; horizontal pod autoscaler will learn the current resource consumption from its status, and will set the desired number of pods by modifying its spec.

        :return: The scale_ref of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: V1beta1SubresourceReference
        """
        return self._scale_ref

    @scale_ref.setter
    def scale_ref(self, scale_ref):
        """
        Sets the scale_ref of this V1beta1HorizontalPodAutoscalerSpec.
        reference to Scale subresource; horizontal pod autoscaler will learn the current resource consumption from its status, and will set the desired number of pods by modifying its spec.

        :param scale_ref: The scale_ref of this V1beta1HorizontalPodAutoscalerSpec.
        :type: V1beta1SubresourceReference
        """

        self._scale_ref = scale_ref

    @property
    def max_replicas(self):
        """
        Gets the max_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :return: The max_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """
        Sets the max_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :param max_replicas: The max_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._max_replicas = max_replicas

    @property
    def min_replicas(self):
        """
        Gets the min_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :return: The min_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """
        Sets the min_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :param min_replicas: The min_replicas of this V1beta1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def cpu_utilization(self):
        """
        Gets the cpu_utilization of this V1beta1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified it defaults to the target CPU utilization at 80% of the requested resources.

        :return: The cpu_utilization of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: V1beta1CPUTargetUtilization
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        """
        Sets the cpu_utilization of this V1beta1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified it defaults to the target CPU utilization at 80% of the requested resources.

        :param cpu_utilization: The cpu_utilization of this V1beta1HorizontalPodAutoscalerSpec.
        :type: V1beta1CPUTargetUtilization
        """

        self._cpu_utilization = cpu_utilization

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
