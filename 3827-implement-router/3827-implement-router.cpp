class Router {
public:
    int memoryLimit;
    deque<tuple<int,int,int>> q; // (source, dest, timestamp)
    unordered_set<string> seen;  // to check duplicates
    unordered_map<int, vector<int>> destMap; // dest -> sorted timestamps

    Router(int memoryLimit) {
        this->memoryLimit = memoryLimit;
    }
    
    string makeKey(int s, int d, int t) {
        return to_string(s) + "#" + to_string(d) + "#" + to_string(t);
    }

    void removeFromDestMap(int dest, int timestamp) {
        auto &arr = destMap[dest];
        auto it = lower_bound(arr.begin(), arr.end(), timestamp);
        if (it != arr.end() && *it == timestamp) {
            arr.erase(it); // O(n) worst-case, but fine for 1e5 ops
        }
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        string key = makeKey(source, destination, timestamp);
        if (seen.count(key)) return false; // duplicate

        // If memory full, evict oldest
        if ((int)q.size() >= memoryLimit) {
            auto [os, od, ot] = q.front();
            q.pop_front();
            seen.erase(makeKey(os, od, ot));
            removeFromDestMap(od, ot);
        }

        // Add new packet
        q.push_back({source, destination, timestamp});
        seen.insert(key);
        destMap[destination].push_back(timestamp); // timestamps always increasing
        return true;
    }
    
    vector<int> forwardPacket() {
        if (q.empty()) return {};
        auto [s, d, t] = q.front();
        q.pop_front();
        seen.erase(makeKey(s, d, t));
        removeFromDestMap(d, t);
        return {s, d, t};
    }
    
    int getCount(int destination, int startTime, int endTime) {
        auto &arr = destMap[destination];
        auto l = lower_bound(arr.begin(), arr.end(), startTime);
        auto r = upper_bound(arr.begin(), arr.end(), endTime);
        return r - l;
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */