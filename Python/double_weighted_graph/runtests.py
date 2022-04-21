#!/usr/bin/env python

import unittest
from testfile import *


class WeightedGraphTests(unittest.TestCase):
    def test_weightedgraph_init(self):
        result = WeightedGraph()
        self.assertIsInstance(result, WeightedGraph, 
                              msg=f"Expected WeightedGraph class but got {type(result)} instead")
        self.assertTrue(hasattr(result, "nodes"), msg="Expected WeightedGraph class member nodes")
        self.assertEqual(type({}), type(result.nodes), 
                         msg=f"Expected nodes to be of type dict but got {type(result.nodes)} instead")
        self.assertDictEqual({}, result.nodes, msg="Mismatch in nodes value")
    
    def test_weightedgraph_add_node_get_nodes_single(self):
        expected_node_id = 7
        expected_graph_data = 14

        result = WeightedGraph()
        self.assertDictEqual({}, result.nodes, msg="Mismatch in nodes value")

        result.add_node(expected_node_id, expected_graph_data)
        self.assertTrue(len(result.nodes) == 1, msg=f"Expected nodes length of 1 but received {len(result.nodes)}")
        self.assertTrue(expected_node_id in result.nodes, msg="Mismatch in nodes value")
        self.assertListEqual([(expected_node_id, expected_graph_data)], result.get_nodes(), 
                             msg=f"Expected node value {expected_graph_data} missing")

    def test_weightedgraph_add_node_get_nodes_multi(self):
        expected_node_id1 = 2
        expected_graph_data1 = 43
        expected_nodes1 = [(expected_node_id1, expected_graph_data1)]
        expected_node_id2 = 22
        expected_graph_data2 = 34
        expected_nodes2 = expected_nodes1 + [(expected_node_id2, expected_graph_data2)]
        expected_node_id3 = 12
        expected_graph_data3 = 21
        expected_nodes3 = expected_nodes2 + [(expected_node_id3, expected_graph_data3)]
        expected_node_id4 = 57
        expected_graph_data4 = 75
        expected_nodes4 = expected_nodes3 + [(expected_node_id4, expected_graph_data4)]

        result = WeightedGraph()
        self.assertDictEqual({}, result.nodes, msg="Mismatch in nodes value")

        result.add_node(expected_node_id1, expected_graph_data1)
        self.assertTrue(len(result.nodes) == 1, msg=f"Expected nodes length of 1 but received {len(result.nodes)}")
        self.assertListEqual(expected_nodes1, result.get_nodes(), msg="Mismatch in expected nodes list value")

        result.add_node(expected_node_id2, expected_graph_data2)
        self.assertTrue(len(result.nodes) == 2, msg=f"Expected nodes length of 2 but received {len(result.nodes)}")
        self.assertListEqual(expected_nodes2, result.get_nodes(), msg="Mismatch in expected nodes list value")

        result.add_node(expected_node_id3, expected_graph_data3)
        self.assertTrue(len(result.nodes) == 3, msg=f"Expected nodes length of 3 but received {len(result.nodes)}")
        self.assertListEqual(expected_nodes3, result.get_nodes(), msg="Mismatch in expected nodes list value")

        result.add_node(expected_node_id4, expected_graph_data4)
        self.assertTrue(len(result.nodes) == 4, msg=f"Expected nodes length of 4 but received {len(result.nodes)}")
        self.assertListEqual(expected_nodes4, result.get_nodes(), msg="Mismatch in expected nodes list value")
    
    def test_weightedgraph_add_edge_get_edges_single(self):
        expected_node_id = 12
        expected_graph_data = 22
        expected_dest_id = 3
        expected_cost = 33

        result = WeightedGraph()
        self.assertDictEqual({}, result.nodes, msg="Mismatch in nodes value")

        result.add_node(expected_node_id, expected_graph_data)
        self.assertTrue(len(result.nodes) == 1, msg=f"Expected nodes length of 1 but received {len(result.nodes)}")
        self.assertTrue(expected_node_id in result.nodes, msg="Mismatch in nodes value")

        result.add_edge(expected_node_id, expected_dest_id, expected_cost)
        self.assertListEqual([(expected_node_id, expected_dest_id, expected_cost)], result.get_edges(), 
                             msg="Mismatch in expected edges list value")

    def test_weightedgraph_add_edge_get_edges_multi(self):
        expected_node_id1 = 0
        expected_graph_data1 = 43
        expected_dest_id1 = 8
        expected_cost1 = 4
        expected_edges1 = [(expected_node_id1, expected_dest_id1, expected_cost1)]
        expected_node_id2 = 22
        expected_graph_data2 = 0
        expected_dest_id2 = 0
        expected_cost2 = 5
        expected_edges2 = expected_edges1 + [(expected_node_id2, expected_dest_id2, expected_cost2)]
        expected_node_id3 = 12
        expected_graph_data3 = 21
        expected_dest_id3 = 15
        expected_cost3 = 0
        expected_edges3 = expected_edges2 + [(expected_node_id3, expected_dest_id3, expected_cost3)]
        expected_node_id4 = 57
        expected_graph_data4 = 75
        expected_dest_id4 = 3
        expected_cost4 = 18
        expected_edges4 = expected_edges3 + [(expected_node_id4, expected_dest_id4, expected_cost4)]

        result = WeightedGraph()
        result.add_node(expected_node_id1, expected_graph_data1)
        result.add_edge(expected_node_id1, expected_dest_id1, expected_cost1)
        self.assertTrue(len(result.nodes) == 1, msg=f"Expected nodes length of 1 but received {len(result.nodes)}")
        self.assertListEqual(expected_edges1, result.get_edges(), msg="Mismatch in expected edges list value")

        result.add_node(expected_node_id2, expected_graph_data2)
        result.add_edge(expected_node_id2, expected_dest_id2, expected_cost2)
        self.assertTrue(len(result.nodes) == 2, msg=f"Expected nodes length of 2 but received {len(result.nodes)}")
        self.assertListEqual(expected_edges2, result.get_edges(), msg="Mismatch in expected edges list value")

        result.add_node(expected_node_id3, expected_graph_data3)
        result.add_edge(expected_node_id3, expected_dest_id3, expected_cost3)
        self.assertTrue(len(result.nodes) == 3, msg=f"Expected nodes length of 3 but received {len(result.nodes)}")
        self.assertListEqual(expected_edges3, result.get_edges(), msg="Mismatch in expected edges list value")

        result.add_node(expected_node_id4, expected_graph_data4)
        result.add_edge(expected_node_id4, expected_dest_id4, expected_cost4)
        self.assertTrue(len(result.nodes) == 4, msg=f"Expected nodes length of 4 but received {len(result.nodes)}")
        self.assertListEqual(expected_edges4, result.get_edges(), msg="Mismatch in expected edges list value")

    def test_weightedgraph_get_nodes_empty(self):
        result = WeightedGraph()
        self.assertListEqual([], result.get_nodes(), msg="Mismatch in expected nodes list value")

    def test_weightedgraph_get_edges_empty(self):
        result = WeightedGraph()
        self.assertListEqual([], result.get_edges(), msg="Mismatch in expected edges list value")

    def test_weightedgraph_delete_node_first(self):
        node1 = 0
        node1_value = 2
        node1_dest_id = 0
        node1_cost = 10
        node2 = 1
        node2_value = 3
        node2_dest_id = 1
        node2_cost = 5
        node3 = 6
        node3_value = 0
        node3_dest_id = 0
        node3_cost = 2
        node4 = 11
        node4_value = 7
        node4_dest_id = 9
        node4_cost = 4
        node5 = 7
        node5_value = 3
        node5_dest_id = 3
        node5_cost = 5

        result = WeightedGraph()
        result.add_node(node1, node1_value)
        result.add_edge(node1, node1_dest_id, node1_cost)
        result.add_node(node2, node2_value)
        result.add_edge(node2, node2_dest_id, node2_cost)
        result.add_node(node3, node3_value)
        result.add_edge(node3, node3_dest_id, node3_cost)
        result.add_node(node4, node4_value)
        result.add_edge(node4, node4_dest_id, node4_cost)
        result.add_node(node5, node5_value)
        result.add_edge(node5, node5_dest_id, node5_cost)

        self.assertListEqual([node1, node2, node3, node4, node5], list(result.nodes.keys()))
        result.delete_node(node1)
        self.assertListEqual([node2, node3, node4, node5], list(result.nodes.keys()))

    def test_weightedgraph_delete_node_last(self):
        node1 = 0
        node1_value = 2
        node1_dest_id = 0
        node1_cost = 10
        node2 = 1
        node2_value = 3
        node2_dest_id = 1
        node2_cost = 5
        node3 = 6
        node3_value = 0
        node3_dest_id = 0
        node3_cost = 2
        node4 = 11
        node4_value = 7
        node4_dest_id = 9
        node4_cost = 4
        node5 = 7
        node5_value = 3
        node5_dest_id = 3
        node5_cost = 5

        result = WeightedGraph()
        result.add_node(node1, node1_value)
        result.add_edge(node1, node1_dest_id, node1_cost)
        result.add_node(node2, node2_value)
        result.add_edge(node2, node2_dest_id, node2_cost)
        result.add_node(node3, node3_value)
        result.add_edge(node3, node3_dest_id, node3_cost)
        result.add_node(node4, node4_value)
        result.add_edge(node4, node4_dest_id, node4_cost)
        result.add_node(node5, node5_value)
        result.add_edge(node5, node5_dest_id, node5_cost)

        self.assertListEqual([node1, node2, node3, node4, node5], list(result.nodes.keys()))
        result.delete_node(node5)
        self.assertListEqual([node1, node2, node3, node4], list(result.nodes.keys()))

    def test_weightedgraph_delete_node_middle(self):
        node1 = 0
        node1_value = 2
        node1_dest_id = 0
        node1_cost = 10
        node2 = 1
        node2_value = 3
        node2_dest_id = 1
        node2_cost = 5
        node3 = 6
        node3_value = 0
        node3_dest_id = 0
        node3_cost = 2
        node4 = 11
        node4_value = 7
        node4_dest_id = 9
        node4_cost = 4
        node5 = 7
        node5_value = 3
        node5_dest_id = 3
        node5_cost = 5

        result = WeightedGraph()
        result.add_node(node1, node1_value)
        result.add_edge(node1, node1_dest_id, node1_cost)
        result.add_node(node2, node2_value)
        result.add_edge(node2, node2_dest_id, node2_cost)
        result.add_node(node3, node3_value)
        result.add_edge(node3, node3_dest_id, node3_cost)
        result.add_node(node4, node4_value)
        result.add_edge(node4, node4_dest_id, node4_cost)
        result.add_node(node5, node5_value)
        result.add_edge(node5, node5_dest_id, node5_cost)

        self.assertListEqual([node1, node2, node3, node4, node5], list(result.nodes.keys()))
        result.delete_node(node3)
        self.assertListEqual([node1, node2, node4, node5], list(result.nodes.keys()))

    def test_weightedgraph_delete_node_nonexistant1(self):
        node1 = 0
        node1_value = 2
        node1_dest_id = 0
        node1_cost = 10
        node2 = 1
        node2_value = 3
        node2_dest_id = 1
        node2_cost = 5
        node3 = 6
        node3_value = 0
        node3_dest_id = 0
        node3_cost = 2
        node4 = 11
        node4_value = 7
        node4_dest_id = 9
        node4_cost = 4
        node5 = 7
        node5_value = 3
        node5_dest_id = 3
        node5_cost = 5

        result = WeightedGraph()
        result.add_node(node1, node1_value)
        result.add_edge(node1, node1_dest_id, node1_cost)
        result.add_node(node2, node2_value)
        result.add_edge(node2, node2_dest_id, node2_cost)
        result.add_node(node3, node3_value)
        result.add_edge(node3, node3_dest_id, node3_cost)
        result.add_node(node4, node4_value)
        result.add_edge(node4, node4_dest_id, node4_cost)
        result.add_node(node5, node5_value)
        result.add_edge(node5, node5_dest_id, node5_cost)

        self.assertListEqual([node1, node2, node3, node4, node5], list(result.nodes.keys()))
        result.delete_node(1234)
        self.assertListEqual([node1, node2, node3, node4, node5], list(result.nodes.keys()))

    def test_weightedgraph_delete_node_nonexistant2(self):
        result = WeightedGraph()

        self.assertListEqual([], list(result.nodes.keys()))
        result.delete_node(4321)
        self.assertListEqual([], list(result.nodes.keys()))

    def test_weightedgraph_delete_node_all(self):
        node1 = 0
        node1_value = 2
        node1_dest_id = 0
        node1_cost = 10
        node2 = 1
        node2_value = 3
        node2_dest_id = 1
        node2_cost = 5
        node3 = 6
        node3_value = 0
        node3_dest_id = 0
        node3_cost = 2
        node4 = 11
        node4_value = 7
        node4_dest_id = 9
        node4_cost = 4
        node5 = 7
        node5_value = 3
        node5_dest_id = 3
        node5_cost = 5

        result = WeightedGraph()
        result.add_node(node1, node1_value)
        result.add_edge(node1, node1_dest_id, node1_cost)
        result.add_node(node2, node2_value)
        result.add_edge(node2, node2_dest_id, node2_cost)
        result.add_node(node3, node3_value)
        result.add_edge(node3, node3_dest_id, node3_cost)
        result.add_node(node4, node4_value)
        result.add_edge(node4, node4_dest_id, node4_cost)
        result.add_node(node5, node5_value)
        result.add_edge(node5, node5_dest_id, node5_cost)

        self.assertListEqual([node1, node2, node3, node4, node5], list(result.nodes.keys()))
        nodes = list(result.nodes.keys())
        for node in nodes:
            result.delete_node(node)
            
        self.assertDictEqual({}, result.nodes, msg=f"Some nodes were not deleted: {result.nodes}")
    
    def test_traverse(self):
        graph = WeightedGraph()
        graph.add_node(0, 5)
        graph.add_node(1, 4)
        graph.add_edge(0, 1, 2)
        graph.add_edge(1, 0, 3)

        graph.add_node(2, 4)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 1, 2)

        graph.add_node(3,9)
        graph.add_edge(0, 3, 1)
        graph.add_edge(3, 3, 2)
        graph.add_edge(2, 3, 2)

        graph.add_node(4, 7)
        graph.add_edge(2, 4, 5)

        graph.add_node(5, 10)
        graph.add_edge(1, 5, 17)
        graph.add_edge(5, 4, 33)


        self.assertTrue(all( item in [(0, 1, 2), (0, 3, 1), (1, 0, 3), (1, 2, 1), (1, 5, 17), (2, 1, 2), (2, 3, 2), 
                                      (2, 4, 5), (3, 3, 2), (5, 4, 33)] for item in graph.get_edges()))

        path = graph.traverse(0, 4)

        self.assertEqual(path, [0, 1, 2, 4])

        self.assertEqual(graph.traverse(4, 0), None)

    def test_traverse_missing_node(self):
        graph = WeightedGraph()
        graph.add_node(0, 5)

        self.assertEqual(graph.traverse(0, 1), None)


class PerformanceTester(unittest.TestCase):
    def test_simple_graph(self):
        two_node_graph_node_check = [(0,5), (1,4)]
        two_node_graph_edge_check = [(0,1,2),(1,0,3)]
        graph = WeightedGraph()
        graph.add_node(0, 5)
        graph.add_node(1, 4)
        graph.add_edge(0, 1, 2)
        graph.add_edge(1, 0, 3)
        self.assertTrue(all(item in two_node_graph_node_check for item in graph.get_nodes()))
        self.assertTrue(all(item in two_node_graph_edge_check for item in graph.get_edges()))

        # delete a node
        graph.delete_node(1)
        self.assertEqual(graph.get_nodes(), [(0,5)])
        self.assertEqual(graph.get_edges(), [])

        # delete the last node
        graph.delete_node(0)
        self.assertEqual(graph.get_nodes(), [])
        self.assertEqual(graph.get_edges(), [])


if __name__ == '__main__':
    unittest.main()
