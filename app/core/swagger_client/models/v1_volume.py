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


class V1Volume(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rbd=None, vsphere_volume=None, glusterfs=None, host_path=None, git_repo=None, azure_disk=None, fc=None, photon_persistent_disk=None, quobyte=None, flocker=None, config_map=None, iscsi=None, flex_volume=None, gce_persistent_disk=None, name=None, nfs=None, azure_file=None, downward_api=None, cephfs=None, persistent_volume_claim=None, cinder=None, aws_elastic_block_store=None, secret=None, empty_dir=None):
        """
        V1Volume - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rbd': 'V1RBDVolumeSource',
            'vsphere_volume': 'V1VsphereVirtualDiskVolumeSource',
            'glusterfs': 'V1GlusterfsVolumeSource',
            'host_path': 'V1HostPathVolumeSource',
            'git_repo': 'V1GitRepoVolumeSource',
            'azure_disk': 'V1AzureDiskVolumeSource',
            'fc': 'V1FCVolumeSource',
            'photon_persistent_disk': 'V1PhotonPersistentDiskVolumeSource',
            'quobyte': 'V1QuobyteVolumeSource',
            'flocker': 'V1FlockerVolumeSource',
            'config_map': 'V1ConfigMapVolumeSource',
            'iscsi': 'V1ISCSIVolumeSource',
            'flex_volume': 'V1FlexVolumeSource',
            'gce_persistent_disk': 'V1GCEPersistentDiskVolumeSource',
            'name': 'str',
            'nfs': 'V1NFSVolumeSource',
            'azure_file': 'V1AzureFileVolumeSource',
            'downward_api': 'V1DownwardAPIVolumeSource',
            'cephfs': 'V1CephFSVolumeSource',
            'persistent_volume_claim': 'V1PersistentVolumeClaimVolumeSource',
            'cinder': 'V1CinderVolumeSource',
            'aws_elastic_block_store': 'V1AWSElasticBlockStoreVolumeSource',
            'secret': 'V1SecretVolumeSource',
            'empty_dir': 'V1EmptyDirVolumeSource'
        }

        self.attribute_map = {
            'rbd': 'rbd',
            'vsphere_volume': 'vsphereVolume',
            'glusterfs': 'glusterfs',
            'host_path': 'hostPath',
            'git_repo': 'gitRepo',
            'azure_disk': 'azureDisk',
            'fc': 'fc',
            'photon_persistent_disk': 'photonPersistentDisk',
            'quobyte': 'quobyte',
            'flocker': 'flocker',
            'config_map': 'configMap',
            'iscsi': 'iscsi',
            'flex_volume': 'flexVolume',
            'gce_persistent_disk': 'gcePersistentDisk',
            'name': 'name',
            'nfs': 'nfs',
            'azure_file': 'azureFile',
            'downward_api': 'downwardAPI',
            'cephfs': 'cephfs',
            'persistent_volume_claim': 'persistentVolumeClaim',
            'cinder': 'cinder',
            'aws_elastic_block_store': 'awsElasticBlockStore',
            'secret': 'secret',
            'empty_dir': 'emptyDir'
        }

        self._rbd = rbd
        self._vsphere_volume = vsphere_volume
        self._glusterfs = glusterfs
        self._host_path = host_path
        self._git_repo = git_repo
        self._azure_disk = azure_disk
        self._fc = fc
        self._photon_persistent_disk = photon_persistent_disk
        self._quobyte = quobyte
        self._flocker = flocker
        self._config_map = config_map
        self._iscsi = iscsi
        self._flex_volume = flex_volume
        self._gce_persistent_disk = gce_persistent_disk
        self._name = name
        self._nfs = nfs
        self._azure_file = azure_file
        self._downward_api = downward_api
        self._cephfs = cephfs
        self._persistent_volume_claim = persistent_volume_claim
        self._cinder = cinder
        self._aws_elastic_block_store = aws_elastic_block_store
        self._secret = secret
        self._empty_dir = empty_dir

    @property
    def rbd(self):
        """
        Gets the rbd of this V1Volume.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :return: The rbd of this V1Volume.
        :rtype: V1RBDVolumeSource
        """
        return self._rbd

    @rbd.setter
    def rbd(self, rbd):
        """
        Sets the rbd of this V1Volume.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :param rbd: The rbd of this V1Volume.
        :type: V1RBDVolumeSource
        """

        self._rbd = rbd

    @property
    def vsphere_volume(self):
        """
        Gets the vsphere_volume of this V1Volume.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :return: The vsphere_volume of this V1Volume.
        :rtype: V1VsphereVirtualDiskVolumeSource
        """
        return self._vsphere_volume

    @vsphere_volume.setter
    def vsphere_volume(self, vsphere_volume):
        """
        Sets the vsphere_volume of this V1Volume.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :param vsphere_volume: The vsphere_volume of this V1Volume.
        :type: V1VsphereVirtualDiskVolumeSource
        """

        self._vsphere_volume = vsphere_volume

    @property
    def glusterfs(self):
        """
        Gets the glusterfs of this V1Volume.
        Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :return: The glusterfs of this V1Volume.
        :rtype: V1GlusterfsVolumeSource
        """
        return self._glusterfs

    @glusterfs.setter
    def glusterfs(self, glusterfs):
        """
        Sets the glusterfs of this V1Volume.
        Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :param glusterfs: The glusterfs of this V1Volume.
        :type: V1GlusterfsVolumeSource
        """

        self._glusterfs = glusterfs

    @property
    def host_path(self):
        """
        Gets the host_path of this V1Volume.
        HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath

        :return: The host_path of this V1Volume.
        :rtype: V1HostPathVolumeSource
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """
        Sets the host_path of this V1Volume.
        HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath

        :param host_path: The host_path of this V1Volume.
        :type: V1HostPathVolumeSource
        """

        self._host_path = host_path

    @property
    def git_repo(self):
        """
        Gets the git_repo of this V1Volume.
        GitRepo represents a git repository at a particular revision.

        :return: The git_repo of this V1Volume.
        :rtype: V1GitRepoVolumeSource
        """
        return self._git_repo

    @git_repo.setter
    def git_repo(self, git_repo):
        """
        Sets the git_repo of this V1Volume.
        GitRepo represents a git repository at a particular revision.

        :param git_repo: The git_repo of this V1Volume.
        :type: V1GitRepoVolumeSource
        """

        self._git_repo = git_repo

    @property
    def azure_disk(self):
        """
        Gets the azure_disk of this V1Volume.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :return: The azure_disk of this V1Volume.
        :rtype: V1AzureDiskVolumeSource
        """
        return self._azure_disk

    @azure_disk.setter
    def azure_disk(self, azure_disk):
        """
        Sets the azure_disk of this V1Volume.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :param azure_disk: The azure_disk of this V1Volume.
        :type: V1AzureDiskVolumeSource
        """

        self._azure_disk = azure_disk

    @property
    def fc(self):
        """
        Gets the fc of this V1Volume.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :return: The fc of this V1Volume.
        :rtype: V1FCVolumeSource
        """
        return self._fc

    @fc.setter
    def fc(self, fc):
        """
        Sets the fc of this V1Volume.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :param fc: The fc of this V1Volume.
        :type: V1FCVolumeSource
        """

        self._fc = fc

    @property
    def photon_persistent_disk(self):
        """
        Gets the photon_persistent_disk of this V1Volume.
        PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

        :return: The photon_persistent_disk of this V1Volume.
        :rtype: V1PhotonPersistentDiskVolumeSource
        """
        return self._photon_persistent_disk

    @photon_persistent_disk.setter
    def photon_persistent_disk(self, photon_persistent_disk):
        """
        Sets the photon_persistent_disk of this V1Volume.
        PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

        :param photon_persistent_disk: The photon_persistent_disk of this V1Volume.
        :type: V1PhotonPersistentDiskVolumeSource
        """

        self._photon_persistent_disk = photon_persistent_disk

    @property
    def quobyte(self):
        """
        Gets the quobyte of this V1Volume.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :return: The quobyte of this V1Volume.
        :rtype: V1QuobyteVolumeSource
        """
        return self._quobyte

    @quobyte.setter
    def quobyte(self, quobyte):
        """
        Sets the quobyte of this V1Volume.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :param quobyte: The quobyte of this V1Volume.
        :type: V1QuobyteVolumeSource
        """

        self._quobyte = quobyte

    @property
    def flocker(self):
        """
        Gets the flocker of this V1Volume.
        Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running

        :return: The flocker of this V1Volume.
        :rtype: V1FlockerVolumeSource
        """
        return self._flocker

    @flocker.setter
    def flocker(self, flocker):
        """
        Sets the flocker of this V1Volume.
        Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running

        :param flocker: The flocker of this V1Volume.
        :type: V1FlockerVolumeSource
        """

        self._flocker = flocker

    @property
    def config_map(self):
        """
        Gets the config_map of this V1Volume.
        ConfigMap represents a configMap that should populate this volume

        :return: The config_map of this V1Volume.
        :rtype: V1ConfigMapVolumeSource
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """
        Sets the config_map of this V1Volume.
        ConfigMap represents a configMap that should populate this volume

        :param config_map: The config_map of this V1Volume.
        :type: V1ConfigMapVolumeSource
        """

        self._config_map = config_map

    @property
    def iscsi(self):
        """
        Gets the iscsi of this V1Volume.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/examples/volumes/iscsi/README.md

        :return: The iscsi of this V1Volume.
        :rtype: V1ISCSIVolumeSource
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """
        Sets the iscsi of this V1Volume.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/examples/volumes/iscsi/README.md

        :param iscsi: The iscsi of this V1Volume.
        :type: V1ISCSIVolumeSource
        """

        self._iscsi = iscsi

    @property
    def flex_volume(self):
        """
        Gets the flex_volume of this V1Volume.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :return: The flex_volume of this V1Volume.
        :rtype: V1FlexVolumeSource
        """
        return self._flex_volume

    @flex_volume.setter
    def flex_volume(self, flex_volume):
        """
        Sets the flex_volume of this V1Volume.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :param flex_volume: The flex_volume of this V1Volume.
        :type: V1FlexVolumeSource
        """

        self._flex_volume = flex_volume

    @property
    def gce_persistent_disk(self):
        """
        Gets the gce_persistent_disk of this V1Volume.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :return: The gce_persistent_disk of this V1Volume.
        :rtype: V1GCEPersistentDiskVolumeSource
        """
        return self._gce_persistent_disk

    @gce_persistent_disk.setter
    def gce_persistent_disk(self, gce_persistent_disk):
        """
        Sets the gce_persistent_disk of this V1Volume.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :param gce_persistent_disk: The gce_persistent_disk of this V1Volume.
        :type: V1GCEPersistentDiskVolumeSource
        """

        self._gce_persistent_disk = gce_persistent_disk

    @property
    def name(self):
        """
        Gets the name of this V1Volume.
        Volume's name. Must be a DNS_LABEL and unique within the pod. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :return: The name of this V1Volume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Volume.
        Volume's name. Must be a DNS_LABEL and unique within the pod. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :param name: The name of this V1Volume.
        :type: str
        """

        self._name = name

    @property
    def nfs(self):
        """
        Gets the nfs of this V1Volume.
        NFS represents an NFS mount on the host that shares a pod's lifetime More info: http://kubernetes.io/docs/user-guide/volumes#nfs

        :return: The nfs of this V1Volume.
        :rtype: V1NFSVolumeSource
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this V1Volume.
        NFS represents an NFS mount on the host that shares a pod's lifetime More info: http://kubernetes.io/docs/user-guide/volumes#nfs

        :param nfs: The nfs of this V1Volume.
        :type: V1NFSVolumeSource
        """

        self._nfs = nfs

    @property
    def azure_file(self):
        """
        Gets the azure_file of this V1Volume.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :return: The azure_file of this V1Volume.
        :rtype: V1AzureFileVolumeSource
        """
        return self._azure_file

    @azure_file.setter
    def azure_file(self, azure_file):
        """
        Sets the azure_file of this V1Volume.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :param azure_file: The azure_file of this V1Volume.
        :type: V1AzureFileVolumeSource
        """

        self._azure_file = azure_file

    @property
    def downward_api(self):
        """
        Gets the downward_api of this V1Volume.
        DownwardAPI represents downward API about the pod that should populate this volume

        :return: The downward_api of this V1Volume.
        :rtype: V1DownwardAPIVolumeSource
        """
        return self._downward_api

    @downward_api.setter
    def downward_api(self, downward_api):
        """
        Sets the downward_api of this V1Volume.
        DownwardAPI represents downward API about the pod that should populate this volume

        :param downward_api: The downward_api of this V1Volume.
        :type: V1DownwardAPIVolumeSource
        """

        self._downward_api = downward_api

    @property
    def cephfs(self):
        """
        Gets the cephfs of this V1Volume.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :return: The cephfs of this V1Volume.
        :rtype: V1CephFSVolumeSource
        """
        return self._cephfs

    @cephfs.setter
    def cephfs(self, cephfs):
        """
        Sets the cephfs of this V1Volume.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :param cephfs: The cephfs of this V1Volume.
        :type: V1CephFSVolumeSource
        """

        self._cephfs = cephfs

    @property
    def persistent_volume_claim(self):
        """
        Gets the persistent_volume_claim of this V1Volume.
        PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#persistentvolumeclaims

        :return: The persistent_volume_claim of this V1Volume.
        :rtype: V1PersistentVolumeClaimVolumeSource
        """
        return self._persistent_volume_claim

    @persistent_volume_claim.setter
    def persistent_volume_claim(self, persistent_volume_claim):
        """
        Sets the persistent_volume_claim of this V1Volume.
        PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#persistentvolumeclaims

        :param persistent_volume_claim: The persistent_volume_claim of this V1Volume.
        :type: V1PersistentVolumeClaimVolumeSource
        """

        self._persistent_volume_claim = persistent_volume_claim

    @property
    def cinder(self):
        """
        Gets the cinder of this V1Volume.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The cinder of this V1Volume.
        :rtype: V1CinderVolumeSource
        """
        return self._cinder

    @cinder.setter
    def cinder(self, cinder):
        """
        Sets the cinder of this V1Volume.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param cinder: The cinder of this V1Volume.
        :type: V1CinderVolumeSource
        """

        self._cinder = cinder

    @property
    def aws_elastic_block_store(self):
        """
        Gets the aws_elastic_block_store of this V1Volume.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        :return: The aws_elastic_block_store of this V1Volume.
        :rtype: V1AWSElasticBlockStoreVolumeSource
        """
        return self._aws_elastic_block_store

    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, aws_elastic_block_store):
        """
        Sets the aws_elastic_block_store of this V1Volume.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        :param aws_elastic_block_store: The aws_elastic_block_store of this V1Volume.
        :type: V1AWSElasticBlockStoreVolumeSource
        """

        self._aws_elastic_block_store = aws_elastic_block_store

    @property
    def secret(self):
        """
        Gets the secret of this V1Volume.
        Secret represents a secret that should populate this volume. More info: http://kubernetes.io/docs/user-guide/volumes#secrets

        :return: The secret of this V1Volume.
        :rtype: V1SecretVolumeSource
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1Volume.
        Secret represents a secret that should populate this volume. More info: http://kubernetes.io/docs/user-guide/volumes#secrets

        :param secret: The secret of this V1Volume.
        :type: V1SecretVolumeSource
        """

        self._secret = secret

    @property
    def empty_dir(self):
        """
        Gets the empty_dir of this V1Volume.
        EmptyDir represents a temporary directory that shares a pod's lifetime. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir

        :return: The empty_dir of this V1Volume.
        :rtype: V1EmptyDirVolumeSource
        """
        return self._empty_dir

    @empty_dir.setter
    def empty_dir(self, empty_dir):
        """
        Sets the empty_dir of this V1Volume.
        EmptyDir represents a temporary directory that shares a pod's lifetime. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir

        :param empty_dir: The empty_dir of this V1Volume.
        :type: V1EmptyDirVolumeSource
        """

        self._empty_dir = empty_dir

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
