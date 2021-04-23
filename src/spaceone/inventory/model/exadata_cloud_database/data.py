from schematics import Model
from schematics.types import ModelType, ListType, StringType,\
                             FloatType, DateTimeType, IntType, \
                             BooleanType

class Tags(Model):
    key = StringType()
    value = StringType()


class DatabaseSoftwareImage(Model):
    id = StringType(deserialize_from='_id')
    region = StringType()
    compartment_name = StringType()
    compartment_id = StringType(deserialize_from='_compartment_id')
    database_version = StringType(deserialize_from='_database_version')
    display_name = StringType(deserialize_from='_display_name')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('PROVISIONING', 'AVAILABLE', 'DELETING',
                                          'DELETED', 'FAILED', 'TERMINATING',
                                          'TERMINATED', 'UPDATING'))
    time_created = DateTimeType(deserialize_from='_time_created')
    image_type = StringType(deserialize_from='_image_type',
                            choices=('GRID_IMAGE', 'DATABASE_IMAGE'))
    image_shape_family = StringType(deserialize_from='_image_shape_family',
                                    choices=('VM_BM_SHAPE', 'EXADATA_SHAPE'))
    patch_set = StringType(deserialize_from='_patch_set')
    freeform_tags = ListType(ModelType(Tags), deserialize_from='_freeform_tags', default=[])
    database_software_image_included_patches = ListType(StringType,
                                                        deserialize_from='_database_software_image_included_patches')
    included_patches_summary = StringType(deserialize_from='_included_patches_summary')
    database_software_image_one_off_patches = ListType(StringType,
                                                       deserialize_from='_database_software_image_one_off_patches')
    ls_inventory = StringType(deserialize_from='_ls_inventory')
    is_upgrade_supported = BooleanType(deserialize_from='_is_upgrade_supported')

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://cloud.oracle.com/dbaas/dbimages/{self.id}?region={self.region}",
        }


class Maintenancewindow(Model):
    preference = StringType(deserialize_from='preference', serialize_when_none=False)
    months = StringType(deserialize_from='months', serialize_when_none=False)
    weeks_of_month = StringType(deserialize_from='weeks_of_month', serialize_when_none=False)
    hours_of_day = StringType(deserialize_from='hours_of_day', serialize_when_none=False)
    days_of_week = StringType(deserialize_from='days_of_week', serialize_when_none=False)
    lead_time_in_week = StringType(deserialize_from='lead_time_in_weeks', serialize_when_none=False)
    display = StringType(deserialize_from='display', serialize_when_none=False)


class MaintenanceRun(Model):
    id = StringType(deserialize_from='id', serialize_when_none=False)
    display_name = StringType(deserialize_from='display_name', serialize_when_none=False)
    description = StringType(deserialize_from='description', serialize_when_none=False)
    lifecycle_state = StringType(deserialize_from='lifecycle_state',
                                 choices=('SCHEDULED', 'IN_PROGRESS', 'SUCCEEDED',
                                          'SKIPPED', 'FAILED', 'UPDATING',
                                          'DELETING', 'DELETED', 'CANCELED'), serialize_when_none=False)
    time_scheduled = DateTimeType(deserialize_from='time_scheduled', serialize_when_none=False)
    time_started = DateTimeType(deserialize_from='time_started', serialize_when_none=False)
    time_ended = DateTimeType(deserialize_from='time_ended', serialize_when_none=False)
    target_resource_type = StringType(deserialize_from='target_resource_type',
                                      choices=('AUTONOMOUS_EXADATA_INFRASTRUCTURE', 'AUTONOMOUS_CONTAINER_DATABASE',
                                               'EXADATA_DB_SYSTEM', 'CLOUD_EXADATA_INFRASTRUCTURE',
                                               'EXACC_INFRASTRUCTURE', 'AUTONOMOUS_DATABASE'), serialize_when_none=False)
    target_resource_id = StringType(deserialize_from='target_resource_id', serialize_when_none=False)
    maintenance_type = StringType(deserialize_from='maintenance_type',
                                  choices=('PLANNED', 'UNPLANNED'), serialize_when_none=False)
    maintenance_subtype = StringType(deserialize_from='maintenance_subtype',
                                     choices=('QUARTERLY', 'HARDWARE', 'CRITICAL',
                                              'INFRASTRUCTURE', 'DATABASE', 'ONEOFF'), serialize_when_none=False)
    maintenance_display = StringType(deserialize_from='maintenance_display', serialize_when_none=False)
    maintenance_alert = StringType(deserialize_from='maintenance_alert', serialize_when_none=False)


class DBHome(Model):
    compartment_id = StringType(deserialize_from='_compartment_id', serialize_when_none=False)
    database_software_image_id = StringType(deserialize_from='_database_software_image_id', serialize_when_none=False)
    db_home_location = StringType(deserialize_from='db_home_location', serialize_when_none=False)
    db_system_id = StringType(deserialize_from='_db_system_id', serialize_when_none=False)
    db_version = StringType(deserialize_from='_db_version', serialize_when_none=False)
    display_name = StringType(deserialize_from='_display_name', serialize_when_none=False)
    id = StringType(deserialize_from='_id')
    kms_key_id = StringType(deserialize_from='_kms_key_id', serialize_when_none=False)
    last_patch_history_entry_id = StringType(deserialize_from='_last_patch_history_entry_id', serialize_when_none=False)
    lifecycle_details = StringType(deserialize_from='_lifecycle_details', serialize_when_none=False)
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=( 'PROVISIONING', 'AVAILABLE', 'UPDATING',
                                           'TERMINATING', 'TERMINATED', 'FAILED'))
    one_off_patches = ListType(StringType, deserialize_from='_one_off_patches')
    time_created = DateTimeType(deserialize_from='_time_created')
    vm_cluster_id = StringType(deserialize_from='_vm_cluster_id', serialize_when_none=False)


class ConnectionStrings(Model):
    all_connection_strings = ListType(ModelType(Tags), deserialize_from='_all_connection_strings', default=[])
    cdb_default = StringType(deserialize_from='_cdb_default')
    cdb_ip_default = StringType(deserialize_from='_cdb_ip_default')


class UpgradeHistory(Model):
    id = StringType(deserialize_from='_id')
    action = StringType(deserialize_from='_action',
                        choices=('PRECHECK', 'UPGRADE', 'ROLLBACK'))
    source = StringType(deserialize_from='_source',
                        choices=('DB_HOME', 'DB_VERSION', 'DB_SOFTWARE_IMAGE'))
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('SUCCEEDED', 'FAILED', 'IN_PROGRESS'))
    lifecycle_details = StringType(deserialize_from='_lifecycle_details')
    target_db_version = StringType(deserialize_from='_target_db_version')
    target_database_software_image_id = StringType(deserialize_from='_target_database_software_image_id')
    target_db_home_id = StringType(deserialize_from='_target_db_home_id')
    source_db_home_id = StringType(deserialize_from='_source_db_home_id')
    time_started = DateTimeType(deserialize_from='_time_started')
    time_ended = DateTimeType(deserialize_from='_time_ended')
    options = StringType(deserialize_from='_options')


class DataGuardAssociation(Model):
    id = StringType(deserialize_from='_id')
    database_id = StringType(deserialize_from='_database_id')
    role = StringType(deserialize_from='_role',
                      choices=('PRIMARY', 'STANDBY', 'DISABLED_STANDBY'))
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('PROVISIONING', 'AVAILABLE',
                                          'UPDATING', 'TERMINATING', 'TERMINATED'))
    lifecycle_details = StringType(deserialize_from='_lifecycle_details')
    peer_db_system_id = StringType(deserialize_from='_peer_db_system_id')
    peer_db_home_id = StringType(deserialize_from='_peer_db_home_id')
    peer_database_id = StringType(deserialize_from='_peer_database_id')
    peer_data_guard_association_id = StringType(deserialize_from='_peer_data_guard_association_id')
    peer_role = StringType(deserialize_from='_peer_role',
                           choices=('PRIMARY', 'STANDBY', 'DISABLED_STANDBY'))
    apply_lag = StringType(deserialize_from='_apply_lag')
    apply_rate = StringType(deserialize_from='_apply_rate')
    protection_mode = StringType(deserialize_from='_protection_mode',
                                 choices=('MAXIMUM_AVAILABILITY',
                                          'MAXIMUM_PERFORMANCE', 'MAXIMUM_PROTECTION'))
    transport_type = StringType(deserialize_from='_transport_type',
                                choices=('SYNC', 'ASYNC', 'FASTSYNC'))
    time_created = DateTimeType(deserialize_from='_time_created')


class Database(Model):
    id = StringType(deserialize_from='_id')
    region = StringType()
    compartment_id = StringType(deserialize_from='_compartment_id')
    character_set = StringType(deserialize_from='_character_set')
    ncharacter_set = StringType(deserialize_from='_ncharacter_set')
    db_home_id = StringType(deserialize_from="_db_home_id")
    db_system_id = StringType(deserialize_from='_db_system_id')
    db_version = StringType(deserialize_from='db_version')
    vm_cluster_id = StringType(deserialize_from='_vm_cluster_id')
    db_name = StringType(deserialize_from='_db_name')
    pdb_name = StringType(deserialize_from='_pdb_name')
    db_workload = StringType(deserialize_from='_db_workload')
    db_unique_name = StringType(deserialize_from='_db_unique_name')
    lifecycle_detail = StringType(deserialize_from='_lifecycle_detail')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('PROVISIONING', 'AVAILABLE', 'UPDATING',
                                          'BACKUP_IN_PROGRESS', 'UPGRADING', 'TERMINATING',
                                          'TERMINATED', 'RESTORE_FAILED', 'FAILED'))
    time_created = DateTimeType(deserialize_from='_time_created')
    last_backup_timestamp = DateTimeType(deserialize_from='_last_backup_timestamp')
    freeform_tags = ListType(ModelType(Tags), deserialize_from='_freeform_tags', default=[])
    connection_strings = ModelType(ConnectionStrings, deserialize_from='_connection_strings')
    kms_key_id = StringType(deserialize_from='_kms_key_id')
    source_database_point_in_time_recovery_timestamp = \
        DateTimeType(deserialize_from='source_database_point_in_time_recovery_timestamp')
    database_software_image_id = StringType(deserialize_from='_database_software_image_id')
    list_upgrade_history = ListType(ModelType(UpgradeHistory), deserialize_from='list_upgrade_history',
                                    default=[])
    list_dataguard_association = ListType(ModelType(DataGuardAssociation), deserialize_from='list_dataguard_association',
                                          default=[])

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://cloud.oracle.com/dbaas/dbsystems/databases/{self.db_home_id}/{self.id}/?region={self.region}",
        }


class ConsoleConnections(Model):
    compartment_id = StringType(deserialize_from='_compartment_id')
    connection_string = StringType(deserialize_from='_connection_string')
    db_node_id = StringType(deserialize_from='_db_node_id')
    fingerprint = StringType(deserialize_from='_fingerprint')
    id = StringType(deserialize_from='_id')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('ACTIVE', 'CREATING', 'DELETED',
                                          'DELETING', 'FAILED'))


class DbNode(Model):
    id = StringType(deserialize_from='_id')
    db_system_id = StringType(deserialize_from='_db_system_id')
    vnic_id = StringType(deserialize_from='_vnid_id')
    backup_vnic_id = StringType(deserialize_from='_backup_vnic_id')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=( 'PROVISIONING', 'AVAILABLE', 'UPDATING',
                                           'STOPPING', 'STOPPED', 'STARTING',
                                           'TERMINATING', 'TERMINATED', 'FAILED'))
    hostname = StringType(deserialize_from='_hostname')
    fault_domain = StringType(deserialize_from='_fault_domain')
    time_created = DateTimeType(deserialize_from='_time_created')
    software_storage_size_in_gb = StringType(deserialize_from='_software_storage_size_in_gb')
    maintenance_type = StringType(deserialize_from='_maintenance_type')
    time_maintenance_window_start = DateTimeType(deserialize_from='_time_maintenance_window_start')
    time_maintenance_window_end = DateTimeType(deserialize_from='_time_maintenance_window_end')
    additional_details = StringType(deserialize_from='_additional_details')
    console_connections = ListType(ModelType(ConsoleConnections), deserialize_from='console_connections', default=[])


class Backup(Model):
    id = StringType(deserialize_from='_id')
    compartment_name = StringType()
    region = StringType()
    compartment_id = StringType(deserialize_from='_compartment_id')
    database_id = StringType(deserialize_from='_database_id')
    display_name = StringType(deserialize_from='_display_name')
    type = StringType(deserialize_from='_type',
                      choices=('INCREMENTAL', 'FULL', 'VIRTUAL_FULL'))
    time_started = DateTimeType(deserialize_from='_time_started')
    time_ended = DateTimeType(deserialize_from='_time_ended')
    lifecycle_details = StringType(deserialize_from='_lifecycle_details')
    availability_domain = StringType(deserialize_from='_availability_domain')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('CREATING', 'ACTIVE', 'DELETING',
                                          'DELETED', 'FAILED', 'RESTORING'))
    database_edition = StringType(deserialize_from='_database_edition',
                                  choices=('STANDARD_EDITION', 'ENTERPRISE_EDITION',
                                           'ENTERPRISE_EDITION_HIGH_PERFORMANCE',
                                           'ENTERPRISE_EDITION_EXTREME_PERFORMANCE'))
    database_size_in_gbs = FloatType(deserialize_from='_database_size_in_gbs')
    shape = StringType(deserialize_from='_shape')
    version = StringType(deserialize_from='version')
    kms_key_id = StringType(deserialize_from='_kms_key_id')

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://cloud.oracle.com/dbaas/backups/{self.id}?region={self.region}",
        }


# list_cloud_vm_cluster_update_history_entries(cloud_vm_cluster_id, **kwargs)
class VmClusterUpdateHistory(Model):
    id = StringType(deserialize_from='_id')
    update_id = StringType(deserialize_from='_update_id')
    update_action = StringType(deserialize_from='_update_action',
                               choices=('ROLLING_APPLY', 'NON_ROLLING_APPLY',
                                        'PRECHECK', 'ROLLBACK'))
    update_type = StringType(deserialize_from='_update_type',
                             choices=('GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'))
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('IN_PROGRESS', 'SUCCEEDED', 'FAILED'))
    lifecycle_details = StringType(deserialize_from='_lifecycle_details')
    time_started = DateTimeType(deserialize_from='_time_started')
    time_completed = DateTimeType(deserialize_from='_time_completed')

# list_cloud_vm_cluster_updates(cloud_vm_cluster_id, **kwargs)
class VmClusterUpdate(Model):
    id = StringType(deserialize_from='_id')
    description = StringType(deserialize_from='_description')
    last_action = StringType(deserialize_from='_last_action')
    available_actions = ListType(StringType, deserialize_from='_available_actions')
    update_type = StringType(deserialize_from='_update_type',
                             choices=('GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'))
    lifecycle_details = StringType(deserialize_from='_lifecycle_details')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('IN_PROGRESS', 'SUCCEEDED', 'FAILED'))
    time_released = DateTimeType(deserialize_from='_time_released')
    version = StringType(deserialize_from='_version')


# list_cloud_vm_clusters(compartment_id, **kwargs)
class CloudVMCluster(Model):
    id = StringType(deserialize_from='_id')
    region = StringType()
    compartment_name = StringType()
    compartment_id = StringType(deserialize_from='_compartment_id')
    availability_domain = StringType(deserialize_from='_availability_domain')
    subnet_id = StringType(deserialize_from='_subnet_id')
    backup_subnet_id = StringType(deserialize_from='_backup_subnet_id')
    nsg_ids = ListType(StringType, deserialize_from='_nsg_ids')
    backup_network_nsg_ids = ListType(StringType, deserialize_from='_backup_network_nsg_ids')
    last_update_history_entry_id = StringType(deserialize_from='_last_update_history_entry_id')
    shape = StringType(deserialize_from='_shape')
    listener_port = StringType(deserialize_from='_listener_port')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('PROVISIONING', 'AVAILABLE', 'UPDATING',
                                          'TERMINATING', 'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'))
    node_count = IntType(deserialize_from='_node_count')
    storage_size_in_gbs = IntType(deserialize_from='_storage_size_in_gbs')
    display_name = StringType(deserialize_from='_display_name')
    time_created = DateTimeType(deserialize_from='_time_created')
    lifecycle_details = StringType(deserialize_from='_lifecycle_details')
    time_zone = StringType(deserialize_from='_time_zone')
    hostname = StringType(deserialize_from='_hostname')
    domain = StringType(deserialize_from='_domain')
    cpu_core_count = StringType(deserialize_from='_cpu_core_count')
    cluster_name = StringType(deserialize_from='_cluster_name')
    data_storage_percentage = IntType(deserialize_from='_data_storage_percentage')
    is_local_backup_enabled = BooleanType(deserialize_from='_is_local_backup_enabled')
    cloud_exadata_infrastructure_id = StringType(deserialize_from='_cloud_exadata_infrastructure_id')
    is_sparse_diskgroup_enabled = BooleanType(deserialize_from='_is_sparse_diskgroup_enabled')
    gi_version = StringType(deserialize_from='_gi_version')
    system_version = StringType(deserialize_from='_system_version')
    ssh_public_keys = ListType(StringType, deserialize_from='_ssh_public_keys')
    license_model = StringType(deserialize_from='_license_model')
    disk_redundancy = StringType(deserialize_from='_disk_redundancy')
    scan_ip_ids = ListType(StringType, deserialize_from='_scan_ip_ids')
    vip_ids = ListType(StringType, deserialize_from='_vip_ids')
    scan_dns_record_id = StringType(deserialize_from='_scan_dns_record_id')
    freeform_tags = ListType(ModelType(Tags), deserialize_from='_freeform_tags', default=[])
    scan_dns_name = StringType(deserialize_from='_scan_dns_name')
    zone_id = StringType(deserialize_from='_zone_id')
    list_update_history = ListType(ModelType(VmClusterUpdateHistory),deserialize_from='list_update_history')
    list_update = ListType(ModelType(VmClusterUpdate), deserialize_from='_list_update')
    # list_db_homes(compartment_id, vm_cluster_id **kwargs)
    list_db_Home = ListType(ModelType(DBHome), deserialize_from='list_db_home', default=[])
    # list_db_nodes(compartment_id, vm_cluster_id **kwargs), list_console_connections(db_node_id, **kwargs)
    list_db_node = ListType(ModelType(DbNode), deserialize_from='list_db_node', default=[])
    '''
    list_databases(compartment_id,db_home_id  **kwargs), list_data_guard_associations(database_id, **kwargs)
    list_database_upgrade_history_entries(database_id, **kwargs), 
    '''
    list_database = ListType(ModelType(Database), deserialize_from='list_database', default=[])
    list_backup = ListType(ModelType(Backup), deserialize_from='list_backup', default=[])

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://cloud.oracle.com/dbaas/cloudVmClusters/{self.id}?region={self.region}",
        }


# list_cloud_exadata_infrastructures(compartment_id, **kwargs)
class CloudExadataInfra(Model):
    region = StringType()
    compartment_name = StringType()
    id = StringType(deserialize_from='_id')
    compartment_id = StringType(deserialize_from='_compartment_id')
    lifecycle_state = StringType(deserialize_from='_lifecycle_state',
                                 choices=('AVAILABLE', 'UPDATING', 'TERMINATING',
                                          'TERMINATED', 'FAILED', 'MAINTENANCE_IN_PROGRESS'))
    display_name = StringType(deserialize_from='_display_name')
    shape = StringType(deserialize_from='_shape')
    version = StringType(default='XP')
    availability_domain = StringType(deserialize_from='_availability_domain')
    compute_count = StringType(deserialize_from='_compute_count')
    storage_count = StringType(deserialize_from='_storage_count')
    total_storage_size_in_gbs = IntType(deserialize_from='_total_storage_size_in_gbs')
    available_storage_size_in_gbs = IntType(deserialize_from='_available_storage_size_in_gbs')
    time_created = DateTimeType(deserialize_from='_time_created')
    lifecycle_details = StringType(deserialize_from='_lifecycle_details')
    maintenance_window = ModelType(Maintenancewindow, deserialize_from='_maintenance_window')
    last_maintenance_run_id = StringType(deserialize_from='_last_maintenance_run_id')
    next_maintenance_run_id = StringType(deserialize_from='_next_maintenance_run_id')
    last_maintenance_run = ModelType(MaintenanceRun, deserialize_from='last_maintenance_run')
    next_maintenance_run = ModelType(MaintenanceRun, deserialize_from='next_maintenance_run')
    freeform_tags = ListType(ModelType(Tags), deserialize_from='_freeform_tags', default=[])
    list_cloud_vm_cluster = ListType(ModelType(CloudVMCluster), deserialize_from='list_cloud_vm_cluster', default=[])
    #list_database_software_images(compartment_id, **kwargs)
    list_software_image = ListType(ModelType(DatabaseSoftwareImage), deserialize_from='list_software_image', default=[])

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://cloud.oracle.com/dbaas/cloudExadataInfrastructures/{self.id}?region={self.region}",
        }