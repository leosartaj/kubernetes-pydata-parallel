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


class V1SELinuxOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, role=None, user=None, level=None):
        """
        V1SELinuxOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'role': 'str',
            'user': 'str',
            'level': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'role': 'role',
            'user': 'user',
            'level': 'level'
        }

        self._type = type
        self._role = role
        self._user = user
        self._level = level

    @property
    def type(self):
        """
        Gets the type of this V1SELinuxOptions.
        Type is a SELinux type label that applies to the container.

        :return: The type of this V1SELinuxOptions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1SELinuxOptions.
        Type is a SELinux type label that applies to the container.

        :param type: The type of this V1SELinuxOptions.
        :type: str
        """

        self._type = type

    @property
    def role(self):
        """
        Gets the role of this V1SELinuxOptions.
        Role is a SELinux role label that applies to the container.

        :return: The role of this V1SELinuxOptions.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this V1SELinuxOptions.
        Role is a SELinux role label that applies to the container.

        :param role: The role of this V1SELinuxOptions.
        :type: str
        """

        self._role = role

    @property
    def user(self):
        """
        Gets the user of this V1SELinuxOptions.
        User is a SELinux user label that applies to the container.

        :return: The user of this V1SELinuxOptions.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1SELinuxOptions.
        User is a SELinux user label that applies to the container.

        :param user: The user of this V1SELinuxOptions.
        :type: str
        """

        self._user = user

    @property
    def level(self):
        """
        Gets the level of this V1SELinuxOptions.
        Level is SELinux level label that applies to the container.

        :return: The level of this V1SELinuxOptions.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this V1SELinuxOptions.
        Level is SELinux level label that applies to the container.

        :param level: The level of this V1SELinuxOptions.
        :type: str
        """

        self._level = level

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
