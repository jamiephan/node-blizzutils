const nodeCascLib = require("bindings")("deps-casclib")
const nodeStormLib = require("bindings")("deps-stormlib")

console.log(nodeCascLib.casclib(), nodeStormLib.stormlib())