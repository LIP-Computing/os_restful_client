# -*- coding: utf-8 -*-

# Copyright 2015 LIP - Lisbon
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

user_roles = {
                "links": {"self": "http://localhost:5000/v3/users/3a8b1c4387664d9488dee661df025b80/projects", "previous": 'null', "next": 'null'}
                , "projects": [{"description": 'null', "links": {"self": "http://localhost:5000/v3/projects/484d3a7eeb4f4462b329c1d0463cf324"}
                        , "enabled": 'true', "id": "484d3a7eeb4f4462b329c1d0463cf324", "parent_id": 'null', "domain_id": "default", "name": "demo"}
                        , {"description": 'null', "links": {"self": "http://localhost:5000/v3/projects/fc0dd0a3c65f4c7c90d3e6dae2aa5a85"}
                        , "enabled": 'true', "id": "fc0dd0a3c65f4c7c90d3e6dae2aa5a85", "parent_id": 'null', "domain_id": "default", "name": "admin"}
                       ]
                  }

role_assignments= [{"scope": {"project": {"id": "484d3a7eeb4f4462b329c1d0463cf324"}},
                                "role": {"id": "1f53a6862bdb4625930a1083bc675c99"},
                                "user": {"id": "3a8b1c4387664d9488dee661df025b80"},
                                "links": {"assignment": "http://localhost:5000/v3/projects/484d3a7eeb4f4462b329c1d0463cf324/users/3a8b1c4387664d9488dee661df025b80/roles/1f53a6862bdb4625930a1083bc675c99"}},
                      {"scope": {"project": {"id": "484d3a7eeb4f4462b329c1d0463cf324"}},
                                "role": {"id": "689169c48da243efb3d23a8fe7e996bc"},
                                "user": {"id": "3a8b1c4387664d9488dee661df025b80"},
                                "links": {"assignment": "http://localhost:5000/v3/projects/484d3a7eeb4f4462b329c1d0463cf324/users/3a8b1c4387664d9488dee661df025b80/roles/689169c48da243efb3d23a8fe7e996bc"}},
                      ]