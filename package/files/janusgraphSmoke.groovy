/*Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License 

  The following file from the Ambari 2.6 branch titan service was used as a template:
  https://github.com/apache/ambari/blob/branch-2.6/ambari-server/src/main/resources/common-services/TITAN/1.0.0/package/files/titanSmoke.groovy
*/

import org.janusgraph.core.JanusGraphFactory


graph = JanusGraphFactory.open("/opt/janusgraph/conf/janusgraph-hbase-solr.properties")
g = graph.traversal()
l = g.V().limit(1).valueMap(true).toList()
graph.close()
